<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isScrolled = ref(false)
const isMenuOpen = ref(false)

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50
}

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
  <header :class="{ 'is-scrolled': isScrolled }">
    <div class="container header-inner">
      <div class="logo">
        <a href="/">
          <img 
            src="https://floodrestorationgeelong.au/wp-content/uploads/2025/10/Logo-1-removebg-preview-300x133.jpg" 
            alt="Flood Restoration Geelong Logo"
          />
        </a>
      </div>

      <nav :class="{ 'is-open': isMenuOpen }">
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/about">About</a></li>
          <li><a href="/emergency-water-restoration-geelong">Emergency Water Restoration</a></li>
          <li><a href="/water-damage-repairs-geelong">Water Damage Repairs</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </nav>

      <div class="cta">
        <a href="#book" class="btn">Book Now</a>
        <button class="menu-toggle" @click="toggleMenu" aria-label="Toggle Menu">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </div>
  </header>
</template>

<style scoped>
header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  background-color: transparent;
  transition: var(--transition-fast);
  padding: 20px 0;
}

header.is-scrolled {
  background-color: var(--white);
  box-shadow: var(--shadow-main);
  padding: 10px 0;
}

.header-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo img {
  height: 60px;
  width: auto;
}

nav ul {
  display: flex;
  gap: 24px;
}

nav ul li a {
  font-weight: 500;
  color: var(--secondary-color);
  font-size: 15px;
}

nav ul li a:hover {
  color: var(--primary-color);
}

.cta {
  display: flex;
  align-items: center;
  gap: 15px;
}

.menu-toggle {
  display: none;
  flex-direction: column;
  gap: 6px;
  background: none;
  border: none;
  cursor: pointer;
}

.menu-toggle span {
  width: 25px;
  height: 2px;
  background-color: var(--secondary-color);
  transition: var(--transition-fast);
}

@media (max-width: 992px) {
  nav {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background-color: var(--white);
    padding: 20px;
    box-shadow: var(--shadow-main);
    display: none;
  }

  nav.is-open {
    display: block;
  }

  nav ul {
    flex-direction: column;
    gap: 15px;
  }

  .menu-toggle {
    display: flex;
  }
}
</style>
