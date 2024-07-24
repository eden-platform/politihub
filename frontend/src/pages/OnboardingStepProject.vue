<template>
  <FormControl
    label="Committee Name"
    placeholder="Executive Committee"
    @update:modelValue="
      (project) => $emit('update:modelValue', { ...modelValue, project })
    "
    v-model="modelValue.project"
  />
</template>
<script>
export default {
  name: 'OnboardingStepProject',
  props: ['modelValue'],
  emits: ['update:modelValue'],
}
</script>
