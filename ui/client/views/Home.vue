<template>
  <div :key=$route.params.id class="page-container">
    <login-form redirect="/profile"></login-form>
  </div>
</template>

<script>
import LoginForm from 'components/LoginForm'

export default {
  components: {
    LoginForm
  }
}
</script>
