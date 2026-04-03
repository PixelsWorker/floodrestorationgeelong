<template>
  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <a href="https://floodrestorationgeelong.au/">
          <img 
            src="https://floodrestorationgeelong.au/wp-content/uploads/2025/10/Logo-1-removebg-preview-300x133.jpg" 
            alt="Flood Restoration Geelong Logo"
            class="footer-logo"
            loading="lazy"
            decoding="async"
            width="300"
            height="133"
          />
        </a>
        <p>Your local Geelong experts in emergency flood recovery and water damage repairs. Available 24/7 for residential and commercial properties.</p>
      </div>

      <div class="footer-links">
        <h3>Quick Links</h3>
        <ul>
          <li><a href="https://floodrestorationgeelong.au/">Home</a></li>
          <li><a href="https://floodrestorationgeelong.au/about">About Us</a></li>
          <li><a href="https://floodrestorationgeelong.au/faqs">Faq's</a></li>
          <li><a href="https://floodrestorationgeelong.au/blogs">Blog's</a></li>
          <li><a href="https://floodrestorationgeelong.au/area-we-service">Area We Service</a></li>
        </ul>
      </div>

      <div class="footer-services">
        <h3>Our Services</h3>
        <ul>
          <li><a href="https://floodrestorationgeelong.au/emergency-water-restoration-geelong">Emergency Restoration</a></li>
          <li><a href="https://floodrestorationgeelong.au/carpet-water-extraction-geelong">Carpet Extraction</a></li>
          <li><a href="https://floodrestorationgeelong.au/mould-remediation-geelong">Mould Remediation</a></li>
          <li><a href="https://floodrestorationgeelong.au/burst-pipes-geelong">Burst Pipes</a></li>
        </ul>
      </div>

      <div class="footer-reach">
        <h3>Reach Us</h3>
        <ul class="reach-list">
          <li>
            <span class="icon">📍</span>
            <span>165a Moorabool St, Geelong VIC 3220, Australia</span>
          </li>
          <li>
            <span class="icon">📞</span>
            <a href="tel:0459338998">0459 338 998</a>
          </li>
          <li>
            <span class="icon">✉️</span>
            <a href="mailto:info@floodrestorationgeelong.au">info@floodrestorationgeelong.au</a>
          </li>
        </ul>
        <div class="iicrc-logo">
          <img src="https://floodrestorationgeelong.au/wp-content/uploads/2025/10/iicrc.webp" alt="IICRC Certified" loading="lazy" decoding="async" width="60" height="60" />
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="container footer-bottom-inner">
        <p>&copy; 2026 Copyright – Flood Restoration Geelong | All rights reserved. | Design By <a href="https://chinedigital.com.au/" target="_blank" rel="noopener">CHINE DIGITAL</a></p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.site-footer {
  background-color: var(--navy);
  color: var(--white);
  padding: 80px 0 0;
  border-top: 5px solid var(--blue);
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1.5fr;
  gap: 40px;
  margin-bottom: 60px;
}

.footer-logo {
  height: 70px;
  margin-bottom: 25px;
}

.footer-brand p {
  opacity: 0.8;
  font-size: 14px;
  line-height: 1.8;
  margin-bottom: 25px;
}

.social-links {
  display: flex;
  gap: 12px;
}

.social-links a {
  width: 36px;
  height: 36px;
  background-color: rgba(255,255,255,0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  color: var(--white);
  transition: all 0.3s;
}

.social-links a:hover {
  background-color: var(--red);
  transform: translateY(-3px);
}

h3 {
  font-size: 18px;
  color: var(--white);
  margin-bottom: 30px;
  position: relative;
  padding-bottom: 15px;
  font-family: 'Poppins', sans-serif;
}

h3::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 40px;
  height: 2px;
  background-color: var(--red);
}

ul {
  padding: 0;
  margin: 0;
}

ul li {
  margin-bottom: 14px;
}

ul li a {
  opacity: 0.8;
  font-size: 14px;
  transition: all 0.3s;
}

ul li a:hover {
  opacity: 1;
  color: var(--blue-light);
  padding-left: 5px;
}

/* Reach Us Section */
.reach-list li {
  display: flex;
  gap: 12px;
  font-size: 14px;
  opacity: 0.9;
  line-height: 1.6;
}

.reach-list .icon {
  font-size: 16px;
  flex-shrink: 0;
}

.reach-list a:hover {
  color: var(--blue-light);
}

.iicrc-logo {
  margin-top: 25px;
}

.iicrc-logo img {
  height: 60px;
  width: auto;
}

.footer-bottom {
  background-color: rgba(0,0,0,0.2);
  padding: 20px 0;
  font-size: 13px;
}

.footer-bottom-inner {
  display: flex;
  justify-content: center;
  text-align: center;
}

.footer-bottom p {
  opacity: 0.7;
  letter-spacing: 0.5px;
}

.footer-bottom a {
  color: var(--blue-light);
  font-weight: 600;
}

@media (max-width: 1200px) {
  .footer-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 50px;
  }
}

@media (max-width: 768px) {
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 40px;
    text-align: center;
  }
  
  h3::after {
    left: 50%;
    transform: translateX(-50%);
  }

  .social-links {
    justify-content: center;
  }

  .reach-list li {
    justify-content: center;
  }
  
  .site-footer {
    padding: 60px 0 0;
  }
  
  h3 {
    margin-bottom: 20px;
  }
}
</style>
