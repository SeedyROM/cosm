import { mock } from '../utils'
import LoginForm from '../../client/components/LoginForm.vue'

describe('LoginForm', () => {
  const wrapper = mock(LoginForm)
  it('should allow a valid login', () => {
    const usernameField = wrapper.find('input[name=username]')
    const passwordField = wrapper.find('input[name=password]')
    const submitButton = wrapper.find('button.logout')

    usernameField.trigger('input', { value: 'admin' })
    passwordField.trigger('input', { value: 'password123' })
    submitButton.trigger('click')

    wrapper.vm.$nextTick(() => {
      console.log('wrapper')
    })
  })
})
