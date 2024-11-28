<script setup lang="ts">
const props = defineProps({
  error: Object
});

// const handleError = () => clearError({ redirect: '/' })
</script>

<template>
  <NuxtLayout>
    <div>
      <div>
        <p>{{ error?.statusCode }}, Error Page</p>
      </div>
    </div>
  </NuxtLayout>
</template>
