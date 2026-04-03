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

const isSubmenuOpen = ref(false)

const toggleSubmenu = () => {
  console.log('Toggling submenu from', isSubmenuOpen.value, 'to', !isSubmenuOpen.value)
  isSubmenuOpen.value = !isSubmenuOpen.value
}

const handleBookClick = (e) => {
  e.preventDefault()
  openQuoteModal()
}
</script>

<template>
  <div class="site-header">
    <div v-if="isMenuOpen" class="menu-backdrop" @click="closeMenu"></div>

    <div class="top-bar" @click.stop>
      <div class="container top-bar-inner">
        <div class="top-bar-left">
          <a href="tel:0459338998" class="top-info-item">
            <span class="icon">📞</span> <span class="phone-number">0459 338 998</span>
          </a>
          <a href="mailto:info@floodrestorationgeelong.au" class="top-info-item hide-mobile">
            <span class="icon">✉️</span> info@floodrestorationgeelong.au
          </a>
        </div>
        <div class="top-bar-right">
        </div>
      </div>
    </div>

    <header @click.stop>
      <div class="container header-inner">
        <div class="logo">
          <a href="https://floodrestorationgeelong.au/" target="_blank" rel="noopener">
            <img 
              src="https://floodrestorationgeelong.au/wp-content/uploads/2025/10/Logo-1-removebg-preview-300x133.jpg" 
              alt="Flood Restoration Geelong Logo"
              width="300"
              height="133"
              decoding="async"
            />
          </a>
        </div>

        <nav :class="{ 'is-open': isMenuOpen }" @click.stop>
          <button class="close-menu" @click="closeMenu" aria-label="Close Menu">&times;</button>
          <ul>
            <li><a href="https://floodrestorationgeelong.au/" @click="closeMenu">Home</a></li>
            <li><a href="https://floodrestorationgeelong.au/about" @click="closeMenu">About</a></li>
            <li><a href="https://floodrestorationgeelong.au/emergency-water-restoration-geelong" @click="closeMenu">Emergency Water Restoration</a></li>
            <li><a href="https://floodrestorationgeelong.au/water-damage-repairs-geelong" @click="closeMenu">Water Damage Repairs</a></li>
            <li class="has-submenu" :class="{ 'is-active': isSubmenuOpen }">
              <button class="submenu-toggle" @click.stop="toggleSubmenu" type="button">
                Services <span class="arrow" :style="{ transform: isSubmenuOpen ? 'rotate(180deg)' : 'none' }">▼</span>
              </button>
              <ul class="submenu" v-show="isSubmenuOpen">
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
          <button class="menu-toggle" @click.stop="toggleMenu" aria-label="Toggle Menu">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </div>
    </header>
  </div>
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

.phone-number {
  font-size: 15px;
  font-weight: 700;
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
  z-index: 2000; 
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

nav ul li a, .submenu-toggle {
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  font-size: 14px;
  color: var(--navy);
  display: flex;
  align-items: center;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}

nav ul li a:hover, .submenu-toggle:hover {
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
    background: #ffffff;
    padding: 80px 20px 40px;
    box-shadow: -10px 0 50px rgba(0,0,0,0.1);
    transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    z-index: 2100;
    overflow-y: auto;
    -webkit-font-smoothing: antialiased;
    transform: translateX(100%) translateZ(0);
    backface-visibility: hidden;
    border-left: 1px solid #eef2f6;
  }

  nav.is-open {
    transform: translateX(0) translateZ(0);
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
    gap: 0;
  }

  nav ul li a, .submenu-toggle {
    font-size: 14px;
    font-weight: 700;
    padding: 14px 0;
    border-bottom: 1px solid #f0f4f8;
    width: 100%;
    color: var(--navy-dark);
    text-align: left;
    justify-content: flex-start;
  }
  
  nav ul li:last-child a {
    border-bottom: none;
  }

  .submenu {
    position: static;
    box-shadow: none;
    opacity: 1;
    visibility: visible;
    transform: none;
    padding: 0 0 0 15px;
    display: flex;
    flex-direction: column;
    background: #fafbfc;
  }

  .submenu-toggle {
    display: flex;
    justify-content: space-between;
    width: 100%;
    background: none;
  }
  
  .arrow {
    position: static !important;
    margin-left: auto;
  }

  .menu-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.15);
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
    box-shadow: 0 4px 10px rgba(0,0, 124, 190, 0.3);
  }

  .logo img {
    height: 55px;
  }

  .phone-number {
    font-size: 17px;
    font-weight: 800;
  }
}

.mobile-call-btn {
  display: none;
}
</style>