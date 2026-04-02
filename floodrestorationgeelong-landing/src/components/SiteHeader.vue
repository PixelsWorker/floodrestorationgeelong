<script setup>
import { ref } from 'vue'

const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}
</script>

<template>
  <!-- Topbar -->
  <div class="topbar">
    <div class="container topbar-inner">
      <span>Geelong's #1 Flood Restoration Experts — IICRC Certified</span>
      <a href="tel:0459338998" class="topbar-phone">📞 0459 338 998</a>
    </div>
  </div>

  <header>
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
          <li><a href="/" @click="isMenuOpen = false">Home</a></li>
          <li><a href="/about" @click="isMenuOpen = false">About</a></li>
          <li><a href="/emergency-water-restoration-geelong" @click="isMenuOpen = false">Emergency Water Restoration</a></li>
          <li><a href="/water-damage-repairs-geelong" @click="isMenuOpen = false">Water Damage Repairs</a></li>
          <li><a href="/contact" @click="isMenuOpen = false">Contact</a></li>
        </ul>
      </nav>

      <div class="cta">
        <a href="#book" class="btn btn-primary">Book Now</a>
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
.topbar {
  background: var(--navy);
  color: var(--white);
  padding: 8px 0;
  font-size: 13px;
  font-weight: 500;
}

.topbar-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.topbar-phone {
  font-weight: 700;
}

header {
  background: var(--white);
  box-shadow: var(--shadow-main);
  position: sticky;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  transition: var(--transition-fast);
  padding: 15px 0;
}

.header-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo img {
  height: 55px;
  width: auto;
}

nav ul {
  display: flex;
  gap: 24px;
}

nav ul li a {
  font-weight: 600;
  color: var(--navy);
  font-size: 15px;
}

nav ul li a:hover {
  color: var(--blue);
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
  background-color: var(--navy);
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

@media (max-width: 576px) {
  .topbar {
    display: none;
  }
}
</style>
