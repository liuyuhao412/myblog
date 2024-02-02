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
log_file = os.path.join(log_file_directory, 'backup_log.txt')


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
    print("Database initialized.")


@cli.command("backup_db")
def backup_db():
    backup_directory = 'MySQL_backup'
    timestamp = datetime.now().strftime("%Y-%m-%d,%Hh%Mm%Ss")
    backup_file = f'{backup_directory}/backup_{timestamp}.sql'

    # 检查目录是否存在
    if not os.path.exists(backup_directory):
        print(f"目录 '{backup_directory}' 不存在，正在创建...")
        os.makedirs(backup_directory)

    try:
        # 配置日志记录，使用绝对路径
        logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # 密码还需修改，有点安全性问题。
        command = [
            'mysqldump',
            '-u', f'{load_config().USERNAME}',
            f'--password={load_config().PASSWORD}',
            f'{load_config().DATABASE}',
            '-r', backup_file
        ]

        # 在 Windows 上使用 CMD，Linux 上使用 Bash
        shell_command = command if platform.system() == 'Windows' else ' '.join(command)
        subprocess.run(shell_command, check=True, shell=True if platform.system() == 'Windows' else False)

        logging.info(f"备份成功完成。文件保存在 {backup_file}")
        # 在备份后添加文件清理逻辑
        cleanup_old_backups(backup_directory)

    except subprocess.CalledProcessError as e:
        logging.error(f"备份期间发生错误：{e}")


@cli.command("restore_db")
def restore_db():
    backup_directory = 'MySQL_backup'

    # 确保备份文件存在
    backup_file = f'{backup_directory}/backup.sql'
    if not os.path.exists(backup_file):
        print(f"备份文件 '{backup_file}' 不存在。请先执行备份操作。")
        return
    try:
        # 密码还需修改，有点安全性问题。
        command = [
            'mysql',
            '-u', f'{load_config().USERNAME}',
            f'--password={load_config().PASSWORD}',
            f'{load_config().DATABASE}',
            '<', backup_file
        ]

        # 在 Windows 上使用 CMD，Linux 上使用 Bash
        shell_command = command if platform.system() == 'Windows' else ' '.join(command)
        subprocess.run(shell_command, check=True, shell=True if platform.system() == 'Windows' else False)

        print("还原成功完成。")
    except subprocess.CalledProcessError as e:
        print(f"还原期间发生错误：{e}")


if __name__ == "__main__":
    cli()
    # application.run()
