<template>
  <div class="page">
    <login-form redirect="/profile"></login-form>
    <p>
      To get started, edit files in <code>./client</code> and save.
    </p>
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
