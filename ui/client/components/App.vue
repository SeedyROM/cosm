<template>
  <section id="app">
    <nav id="navbar" class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <div class="brand-logo">cosm</div>
        <div class="navbar-burger burger" data-target="navbar-items">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
      <div class="navbar-menu animated" id="navbar-items">
        <div class="navbar-end">
          <router-link class="navbar-item" to="/">Home</router-link>
          <router-link class="navbar-item" to="/profile">Profile</router-link>
        </div>
      </div>
    </nav>
    <transition name="fade" mode="out-in">
      <router-view></router-view>
    </transition>
  </section>
</template>

<script>
document.addEventListener('DOMContentLoaded', function () {
  // Get all "navbar-burger" elements
  var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0)
  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {
    // Add a click event on each of them
    $navbarBurgers.forEach(function ($el) {
      $el.addEventListener('click', function () {
        // Get the target from the "data-target" attribute
        var target = $el.dataset.target
        console.log(target)
        var $target = document.getElementById(target)
        // Toggle the class on both the "navbar-burger" and the "navbar-menu"
        $el.classList.toggle('is-active')
        $target.classList.toggle('is-active')
      })
    })
  }
})
</script>

<style src="../styles/site.scss" lang="scss"></style>
