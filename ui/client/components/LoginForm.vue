<template>
<div class="login-form">
    <div class="logged-in" v-if=$store.state.loggedIn>
        <div class="box">
            You're already logged in as {{ $store.state.username }}.
        </div>
        <div class="field">
            <button class="logout button is-link" v-on:click="$store.dispatch('logout')">Log out</button>
        </div>
    </div>
    <form @submit=submit>
        <div class="error" v-if="error">
            {{ error }}
        </div>
        <div v-if=!$store.state.loggedIn>
            <div class="field">
                <label class="label">Username:</label>
                <input class="input" type="text" name="username" placeholder="Username..." v-model=username>
            </div>
            <div class="field">
                <label class="label">Password:</label>
                <input class="input" type="password" name="password" placeholder="Password..." v-model=password>
            </div>
            <button class="button is-link">Login</button>
        </div>
    </form>
</div>
</template>

<style lang="scss">
    .login-form {
        margin-bottom: 1.5rem;
        .error {
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            background-color: rgb(244, 66, 66);
            color: white;
        }
    }
</style>

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