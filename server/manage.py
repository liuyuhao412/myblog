from flask.cli import FlaskGroup
from app import create_app, db
from app.config import load_config
from flask_migrate import Migrate
from datetime import datetime
import app.models
import subprocess
import platform
import logging
import os


application = create_app()
cli = FlaskGroup(application)
migrate = Migrate(application, db)

log_file_directory = os.path.join(os.path.dirname(__file__), 'logging')
log_file_info = os.path.join(log_file_directory, 'manage.log')
file_info = logging.FileHandler(log_file_info)
file_info.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s', datefmt='%d/%b/%Y %H:%M:%S'))

if not logging.getLogger().handlers:
    # 添加日志处理器到根日志对象
    logging.getLogger().addHandler(file_info)

    # 设置根日志级别
    logging.getLogger().setLevel(logging.DEBUG)


if not os.path.exists(log_file_directory):
    print(f"目录 '{log_file_directory}' 不存在，正在创建...")
    os.makedirs(log_file_directory)


def cleanup_old_backups(backup_directory):
    # 保留最近的几个备份，可以根据需要调整
    keep_latest_n = 5

    # 获取备份目录下所有文件
    all_backups = [f for f in os.listdir(backup_directory) if os.path.isfile(os.path.join(backup_directory, f))]

    # 按照文件名的时间戳排序
    all_backups.sort(reverse=True)

    # 删除超出保留数量的旧备份文件
    for old_backup in all_backups[keep_latest_n:]:
        old_backup_path = os.path.join(backup_directory, old_backup)
        os.remove(old_backup_path)
        logging.info(f"删除旧备份文件: {old_backup}")


@cli.command("init_db")
def init_db():
    """初始化数据库"""
    db.drop_all()
    db.create_all()
    logging.info(f"数据库初始化成功")
    print("数据库初始化成功")


@cli.command("backup_db")
def backup_db():
    backup_directory = 'MySQL_backup'
    timestamp = datetime.now().strftime("%Y-%m-%d-%Hh%Mm%Ss")
    backup_file = f'{backup_directory}/backup_{timestamp}.sql'

    # 检查目录是否存在
    if not os.path.exists(backup_directory):
        print(f"目录 '{backup_directory}' 不存在，正在创建...")
        os.makedirs(backup_directory)

    try:
        # 密码还需修改，有点安全性问题。
        command = [
            'mysqldump',
            '--defaults-file=my.cnf',  # 指定配置文件
            f'{load_config().DATABASE}',
            '-r', backup_file
        ]

        # 在 Windows 上使用 CMD，Linux 上使用 Bash
        shell_command = command if platform.system() == 'Windows' else ' '.join(command)
        subprocess.run(shell_command, check=True, shell=True if platform.system() == 'Windows' else False)

        logging.info(f"备份成功完成。文件保存在 {backup_file}")
        print("备份成功完成")
        # 在备份后添加文件清理逻辑
        cleanup_old_backups(backup_directory)

    except subprocess.CalledProcessError as e:
        logging.error(f"备份期间发生错误：{e}")


@cli.command("restore_db")
def restore_db(backup_file_path=None):
    backup_directory = 'MySQL_backup'

    if backup_file_path is None:
        all_backups = [f for f in os.listdir(backup_directory) if os.path.isfile(os.path.join(backup_directory, f))]
        all_backups.sort(reverse=True)
        if not all_backups:
            print("没有找到备份文件。请先执行备份操作。")
            return
        backup_file_path = os.path.join(backup_directory, all_backups[0])

    try:
        # 密码还需修改，有点安全性问题。
        command = [
            'mysql',
            '--defaults-file=my.cnf',  # 指定配置文件
            f'{load_config().DATABASE}',
            '<', backup_file_path
        ]

        # 在 Windows 上使用 CMD，Linux 上使用 Bash
        shell_command = command if platform.system() == 'Windows' else ' '.join(command)
        subprocess.run(shell_command, check=True, shell=True if platform.system() == 'Windows' else False)
        logging.info(f"还原成功完成。还原文件为 {backup_file_path}")
        print("还原成功完成")
    except subprocess.CalledProcessError as e:
        logging.error(f"备份期间发生错误：{e}")


if __name__ == "__main__":
    cli()
