<template>
  <el-dialog
    v-model="localModelValue"
    :title="''"
    :modal="true"
    :close-on-click-modal="false"
    width="300px"
    :before-close="handleClose"
  >
    <template v-slot:header>
      <div class="dialog-title">{{ dialogProps.title }}</div>
    </template>
    <slot></slot>
  </el-dialog>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref, watch } from "vue";
interface Props {
  title: string;
  modelValue: boolean;
}
const dialogProps = defineProps<Props>();
const emit = defineEmits(["update:modelValue"]);
// 使用 ref 创建本地变量
const localModelValue = ref(dialogProps.modelValue);

// 在组件初始化时将 props 复制给本地变量
watch(
  () => dialogProps.modelValue,
  (newValue) => {
    localModelValue.value = newValue;
  }
);

const handleClose = (): void => {
  emit("update:modelValue", false);
};
</script>

<style scoped>
.dialog-title {
  text-align: center;
  font-size: 30px;
  margin-top: 20px;
}
</style>
