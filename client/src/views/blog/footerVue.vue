<template>
  <div class="wrapper">
    <div class="text">
      <p>若有疑问，请随时联系我们,联系方式如下：</p>
      <ul class="contact-info">
        <li>QQ: 1944669201</li>
        <li>邮箱: liuyuhaoweb@163.com</li>
        <li>地址: XXX省XXX市XXX区XXX道XXX号</li>
        <li>电话: XXX-XXXX-XXXX</li>
      </ul>
      <p>备案号:冀ICP备XXXXXXXX号</p>
      <p>Copyright © 水墨轩 该博客为本人开发和测试使用，仅供学习参考。</p>
    </div>
  </div>
</template>

<script lang="ts" setup></script>
<style scoped>
.wrapper {
  background-color: rgba(67, 138, 126, 0.5);
  width: 1200px;
  margin: 0 auto;
  height: auto;
  padding: 20px 0;
}

.text {
  margin-left: 50px;
  color: white;
}
p {
  margin-bottom: 5px;
}

.contact-info li {
  margin-bottom: 5px;
  margin-left: 30px;
  list-style: none;
}

.contact-info a {
  color: white;
  text-decoration: none;
}
</style>
