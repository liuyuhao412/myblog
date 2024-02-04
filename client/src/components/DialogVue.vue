<template>
  <el-dialog :modelValue="modelValue" :title="dialogProps.dialogTitle">
    <slot></slot>
  </el-dialog>
</template>

<script setup lang="ts">
import { defineProps } from "vue";

interface Props {
  dialogTitle: string;
  modelValue: boolean;
}

const dialogProps = defineProps<Props>();
</script>
