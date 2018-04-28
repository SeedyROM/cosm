import { routeMock } from '../utils'
import Home from '../../client/views/Home.vue'

describe('Home.vue', () => {
  it('Home renders correctly', () => {
    const wrapper = routeMock(Home)
    expect(wrapper.find('h1').text()).toMatch('Welcome home!')
  })
})
