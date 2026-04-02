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
        <div class="social-links">
          <a href="https://facebook.com" target="_blank" aria-label="Facebook"><svg viewBox="0 0 320 512" width="14"><path fill="currentColor" d="M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z"/></svg></a>
          <a href="https://instagram.com" target="_blank" aria-label="Instagram"><svg viewBox="0 0 448 512" width="14"><path fill="currentColor" d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"/></svg></a>
          <a href="https://youtube.com" target="_blank" aria-label="YouTube"><svg viewBox="0 0 576 512" width="14"><path fill="currentColor" d="M549.655 124.083c-6.281-23.65-24.787-42.276-48.284-48.597C458.781 64 288 64 288 64S117.22 64 74.629 75.486c-23.497 6.322-42.003 24.947-48.284 48.597-11.412 42.867-11.412 131.917-11.412 131.917s0 89.05 11.412 131.917c6.281 23.65 24.787 41.504 48.284 47.825C117.22 448 288 448 288 448s170.781 0 213.371-11.486c23.497-6.321 42.003-24.175 48.284-47.825 11.412-42.867 11.412-131.917 11.412-131.917s0-89.05-11.412-131.917zM232 337.687V174.313L373.49 256 232 337.687z"/></svg></a>
        </div>
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
            <a href="#" @click.prevent>Services <span class="arrow">▼</span></a>
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
        <a href="https://floodrestorationgeelong.au/contact" class="btn-book">Book Now</a>
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
}
</style>
