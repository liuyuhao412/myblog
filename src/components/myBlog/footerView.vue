<template>
  <el-footer class="footer">
    <p>&copy; 2024 个人博客</p>
    <p>
      Github:
      <a href="https://github.com/liuyuhao412" target="_blank" class="footer-link"
        >liuyuhao412</a
      >
    </p>
  </el-footer>
</template>

<style scoped>
.footer {
  color: #fff;
  margin-top: 20px;
  padding: 6px 0;
  text-align: center;
  border-radius: 0 0 12px 12px;
  box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.1);
  background: linear-gradient(90deg, #1e90ff, #4169e1);
}

.footer p {
  margin: 0;
  line-height: 1.5;
}

.footer a {
  color: #dfe6ff;
  text-decoration: none;
  font-weight: bold;
}

.footer a:hover {
  text-decoration: underline;
}
</style>
