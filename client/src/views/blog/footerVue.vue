<template>
  <div class="wrapper">
    <div class="text">
      <p>Copyright © 水墨轩 该博客为本人开发和测试使用，仅供学习参考。</p>
      <p>若有疑问，请随时联系我们。联系方式如下：</p>
      <ul class="contact-info">
        <li>QQ: 1944669201</li>
        <li>
          邮箱: <a href="mailto:liuyuhaoweb@163.com">liuyuhaoweb@163.com</a>
        </li>
        <li>地址: XXX省XXX市XXX区XXX道XXX号</li>
        <li>电话: 151-2823-6205</li>
        <li>
          备案号：<a href="http://www.beian.miit.gov.cn" target="_blank"
            >冀ICP备XXXXXXXX号</a
          >
        </li>
      </ul>
      <p>关注我：</p>
      <ul class="social-icons">
        <li>
          <a href="https://github.com/liuyuhao412">
            <i class="fab fa-github"></i> GitHub
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts" setup></script>
<style scoped>
.wrapper {
  background-color: #438a7e;
  width: 1200px;
  margin: 0 auto;
  height: auto;
  padding: 20px 0;
}

.text {
  text-align: center;
  color: white;
}
p {
  margin-bottom: 5px;
}

.contact-info li,
.social-icons li {
  margin-bottom: 5px;
  list-style: none;
}

.contact-info a,
.social-icons a {
  color: white;
  text-decoration: none;
}

.social-icons i {
  margin-right: 50px;
}
</style>
