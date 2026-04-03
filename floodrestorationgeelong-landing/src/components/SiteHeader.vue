<script setup>
import { ref, inject } from 'vue'

const openQuoteModal = inject('openQuoteModal')
const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = () => {
  isMenuOpen.value = false
}

const toggleSubmenu = (e) => {
  e.currentTarget.parentElement.classList.toggle('is-active')
}

const handleBookClick = (e) => {
  e.preventDefault()
  openQuoteModal()
}
</script>

<template>
  <!-- Topbar -->
  <div v-if="isMenuOpen" class="menu-backdrop" @click="closeMenu"></div>
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div class="top-bar-left">
        <a href="tel:0459338998" class="top-info-item">
          <span class="icon">📞</span> 0459 338 998
        </a>
        <a href="mailto:info@floodrestorationgeelong.au" class="top-info-item hide-mobile">
          <span class="icon">✉️</span> info@floodrestorationgeelong.au
        </a>
      </div>
      <div class="top-bar-right">
      </div>
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
        <button class="close-menu" @click="closeMenu" aria-label="Close Menu">&times;</button>
        <ul>
          <li><a href="https://floodrestorationgeelong.au/" @click="closeMenu">Home</a></li>
          <li><a href="https://floodrestorationgeelong.au/about" @click="closeMenu">About</a></li>
          <li><a href="https://floodrestorationgeelong.au/emergency-water-restoration-geelong" @click="closeMenu">Emergency Water Restoration</a></li>
          <li><a href="https://floodrestorationgeelong.au/water-damage-repairs-geelong" @click="closeMenu">Water Damage Repairs</a></li>
          <li class="has-submenu">
            <a href="#" @click.prevent="toggleSubmenu">Services <span class="arrow">▼</span></a>
            <ul class="submenu">
              <li><a href="https://floodrestorationgeelong.au/carpet-drying-geelong" @click="closeMenu">Carpet Drying</a></li>
              <li><a href="https://floodrestorationgeelong.au/carpet-water-extraction-geelong" @click="closeMenu">Carpet Water Extraction</a></li>
              <li><a href="https://floodrestorationgeelong.au/flood-damage-restoration-geelong" @click="closeMenu">Flood Damage Restoration</a></li>
              <li><a href="https://floodrestorationgeelong.au/mould-remediation-geelong" @click="closeMenu">Mould Remediation</a></li>
              <li><a href="https://floodrestorationgeelong.au/burst-pipes-geelong" @click="closeMenu">Burst Pipes</a></li>
            </ul>
          </li>
          <li><a href="https://floodrestorationgeelong.au/blogs" @click="closeMenu">Blogs</a></li>
          <li><a href="https://floodrestorationgeelong.au/contact-flood-restoration-geelong" @click="closeMenu">Contact</a></li>
        </ul>
      </nav>

      <div class="cta-group">
        <a href="tel:0459338998" class="mobile-call-btn" aria-label="Call Now">📞</a>
        <a href="https://floodrestorationgeelong.au/contact" class="btn-book" @click="handleBookClick">Book Now</a>
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
.top-bar {
  background: var(--navy);
  color: var(--white);
  padding: 10px 0;
  font-size: 13px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

.top-bar-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.top-bar-left {
  display: flex;
  gap: 25px;
}

.top-info-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 500;
  transition: opacity 0.2s;
}

.top-info-item:hover {
  opacity: 0.8;
}

.social-links {
  display: flex;
  gap: 15px;
}

.social-links a {
  color: var(--white);
  transition: transform 0.2s;
}

.social-links a:hover {
  transform: translateY(-2px);
}

header {
  background: var(--white);
  box-shadow: 0 2px 15px rgba(0,0,0,0.05);
  position: sticky;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  padding: 12px 0;
}

.header-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo img {
  height: 65px;
  width: auto;
}

nav ul {
  display: flex;
  gap: 22px;
}

nav ul li {
  position: relative;
}

nav ul li a {
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  font-size: 14px;
  color: var(--navy);
  display: flex;
  align-items: center;
  gap: 5px;
}

nav ul li a:hover {
  color: var(--blue);
}

.arrow {
  font-size: 8px;
  transition: transform 0.3s;
}

/* Submenu Styles */
.submenu {
  position: absolute;
  top: 100%;
  left: 0;
  background: var(--white);
  min-width: 240px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  border-radius: 4px;
  padding: 15px 0;
  display: flex;
  flex-direction: column;
  gap: 0;
  opacity: 0;
  visibility: hidden;
  transform: translateY(10px);
  transition: all 0.3s ease;
  z-index: 100;
}

.has-submenu:hover .submenu {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.has-submenu:hover .arrow {
  transform: rotate(180deg);
}

.submenu li a {
  padding: 10px 20px;
  font-size: 13px;
  font-weight: 500;
  border-bottom: 1px solid #f5f5f5;
}

.submenu li:last-child a {
  border-bottom: none;
}

.submenu li a:hover {
  background: #f8fbff;
  padding-left: 25px;
}

.cta-group {
  display: flex;
  align-items: center;
  gap: 15px;
}

.btn-book {
  background: var(--red);
  color: var(--white);
  padding: 10px 22px;
  border-radius: 4px;
  font-family: 'Poppins', sans-serif;
  font-weight: 700;
  font-size: 14px;
  text-transform: uppercase;
  transition: all 0.3s;
}

.btn-book:hover {
  background: var(--navy);
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(227, 30, 36, 0.2);
}

.close-menu {
  display: none;
}

.menu-toggle {
  display: none;
  flex-direction: column;
  gap: 5px;
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
}

@media (max-width: 1100px) {
  nav ul { gap: 15px; }
  nav ul li a { font-size: 13px; }
}

@media (max-width: 992px) {
  .top-bar .hide-mobile { display: none; }
  
  .btn-book { display: none; }
  .menu-toggle { display: flex; }

  nav {
    position: fixed;
    top: 0;
    right: 0;
    width: 280px;
    height: 100vh;
    background: var(--white);
    padding: 80px 25px 60px;
    box-shadow: -10px 0 50px rgba(0,0,0,0.1);
    transform: translateX(100%);
    transition: transform 0.4s ease;
    z-index: 2000;
  }

  nav.is-open {
    transform: translateX(0);
  }

  .close-menu {
    display: block;
    position: absolute;
    top: 20px;
    right: 20px;
    background: none;
    border: none;
    font-size: 32px;
    line-height: 1;
    color: var(--navy);
    cursor: pointer;
    padding: 5px;
  }

  nav ul {
    flex-direction: column;
    gap: 15px;
  }

  nav ul li a {
    font-size: 16px;
    padding: 8px 0;
  }

  .submenu {
    position: static;
    box-shadow: none;
    opacity: 1;
    visibility: visible;
    transform: none;
    padding: 10px 0 10px 15px;
    display: none;
  }

  .has-submenu.is-active .submenu {
    display: flex;
  }

  .menu-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(7, 26, 48, 0.4);
    backdrop-filter: blur(2px);
    z-index: 1500;
  }

  .mobile-call-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    background: var(--blue);
    color: var(--white);
    border-radius: 50%;
    font-size: 18px;
    box-shadow: 0 4px 10px rgba(0, 124, 190, 0.3);
  }

  .logo img {
    height: 45px;
  }
}

.mobile-call-btn {
  display: none;
}
</style>
