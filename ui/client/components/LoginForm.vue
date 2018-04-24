<template>
<form @submit=submit>
    <div class="logged-in" v-if=$store.state.loggedIn>
        You're already logged in as {{ $store.state.username }}.
        <button class="logout" v-on:click="$store.dispatch('logout')">Log out</button>
    </div>
    <div class="error" v-if="error">
        {{ error }}
    </div>
    <div v-if=!$store.state.loggedIn>
        <input type="text" name="username" placeholder="Username..." v-model=username>
        <input type="password" name="password" placeholder="Password..." v-model=password>
        <button>Login</button>
    </div>
</form>
</template>

<script>
export default {
    props: ['redirect'],
    data: function() {
        return {
            username: '',
            password: '',
            error: null
        }
    },
    methods: {
        submit(event) {
            event.preventDefault()

            if(this.username.length == 0 && this.password.length == 0) {
                this.error = 'Both username and password are required.'
                return false
            }

            this.axios
            .post(
            '//localhost:8000/api/v1/authentication/obtain_token/',
            { username: this.username, password: this.password }
            )
            .then(({ data }) => {
                this.error = null
                this.$store.dispatch('authenticate', { 
                    data: data.token,
                    username: this.username
                })
                if(this.redirect) {
                    this.$router.push(this.redirect)
                }
            })
            .catch(({ response }) => {
                this.error = 'Unable to login with given username and password.'
            })

            return false
        }
    }
}
</script>