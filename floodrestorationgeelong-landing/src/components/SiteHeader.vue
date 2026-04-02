<script setup>
import { ref } from 'vue'

const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = () => {
  isMenuOpen.value = false
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
        <a href="https://floodrestorationgeelong.au/" target="_blank" rel="noopener">
          <img 
            src="https://floodrestorationgeelong.au/wp-content/uploads/2025/10/Logo-1-removebg-preview-300x133.jpg" 
            alt="Flood Restoration Geelong Logo"
          />
        </a>
      </div>

      <nav :class="{ 'is-open': isMenuOpen }">
        <ul>
          <li><a href="https://floodrestorationgeelong.au/" target="_blank" rel="noopener" @click="closeMenu">Home</a></li>
          <li><a href="https://floodrestorationgeelong.au/about" target="_blank" rel="noopener" @click="closeMenu">About</a></li>
          <li><a href="https://floodrestorationgeelong.au/emergency-water-restoration-geelong" target="_blank" rel="noopener" @click="closeMenu">Emergency Water Restoration</a></li>
          <li><a href="https://floodrestorationgeelong.au/water-damage-repairs-geelong" target="_blank" rel="noopener" @click="closeMenu">Water Damage Repairs</a></li>
          <li><a href="https://floodrestorationgeelong.au/contact" target="_blank" rel="noopener" @click="closeMenu">Contact</a></li>
        </ul>
      </nav>

      <div class="cta">
        <a href="https://floodrestorationgeelong.au/contact" target="_blank" rel="noopener" class="btn btn-primary">Book Now</a>
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
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  font-size: 15px;
  color: var(--navy);
}

nav ul li a:hover {
  color: var(--blue);
}

.menu-toggle {
  display: none;
  flex-direction: column;
  gap: 6px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 5px;
}

.menu-toggle span {
  display: block;
  width: 25px;
  height: 2px;
  background: var(--navy);
  transition: var(--transition-fast);
}

@media (max-width: 992px) {
  .cta .btn {
    display: none;
  }
  
  .menu-toggle {
    display: flex;
  }

  nav {
    position: fixed;
    top: 100px;
    left: 0;
    width: 100%;
    background: var(--white);
    padding: 40px 24px;
    box-shadow: var(--shadow-main);
    transform: translateY(-110%);
    transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }

  nav.is-open {
    transform: translateY(0);
  }

  nav ul {
    flex-direction: column;
    gap: 20px;
    text-align: center;
  }

  nav ul li a {
    font-size: 18px;
    display: block;
    padding: 10px 0;
  }
}
</style>
