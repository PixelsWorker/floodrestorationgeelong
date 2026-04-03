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
        
        <div class="social-links">
          <a href="https://www.facebook.com/FloodRestorationsGeelong" target="_blank" rel="noopener" aria-label="Facebook">FB</a>
          <a href="https://www.instagram.com/flood_restorationgeelong/" target="_blank" rel="noopener" aria-label="Instagram">IG</a>
          <a href="https://www.youtube.com/@FloodRestorationGeelong" target="_blank" rel="noopener" aria-label="YouTube">YT</a>
          <a href="https://share.google/2klbNcAy39ABHeqaf" target="_blank" rel="noopener" aria-label="Google Reviews">G+</a>
        </div>
      </div>

      <div class="footer-links">
        <h3>Quick Links</h3>
        <ul>
          <li><a href="https://floodrestorationgeelong.au/">Home</a></li>
          <li><a href="https://floodrestorationgeelong.au/about">About Us</a></li>
          <li><a href="https://floodrestorationgeelong.au/faqs">FAQ's</a></li>
          <li><a href="https://floodrestorationgeelong.au/blogs">Blog</a></li>
          <li><a href="https://floodrestorationgeelong.au/area-we-service">Areas We Service</a></li>
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
            <span class="text">165a Moorabool St, Geelong VIC 3220, Australia</span>
          </li>
          <li>
            <span class="icon">📞</span>
            <a href="tel:0459338998" class="text">0459 338 998</a>
          </li>
          <li>
            <span class="icon">✉️</span>
            <a href="mailto:info@floodrestorationgeelong.au" class="text">info@floodrestorationgeelong.au</a>
          </li>
        </ul>
        <div class="iicrc-logo">
          <img src="https://floodrestorationgeelong.au/wp-content/uploads/2025/10/iicrc-150x150.webp" alt="IICRC Certified" loading="lazy" decoding="async" width="120" height="120" />
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
  background-color: var(--navy, #0a192f); /* Added fallback color */
  color: var(--white, #ffffff);
  padding: 80px 0 0;
  border-top: 5px solid var(--blue, #007cbe);
  font-family: 'Inter', 'Poppins', sans-serif;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1.5fr;
  gap: 50px;
  margin-bottom: 60px;
}

.footer-logo {
  height: 75px;
  width: auto;
  margin-bottom: 25px;
  filter: brightness(1.1); /* Makes logo pop slightly on dark bg */
}

.footer-brand p {
  opacity: 0.8;
  font-size: 14px;
  line-height: 1.8;
  margin-bottom: 25px;
  max-width: 90%;
}

.social-links {
  display: flex;
  gap: 12px;
}

.social-links a {
  width: 40px;
  height: 40px;
  background-color: rgba(255, 255, 255, 0.08);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%; /* Circles look cleaner */
  color: var(--white, #fff);
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.3s ease;
}

.social-links a:hover {
  background-color: var(--red, #e31e24);
  transform: translateY(-4px);
  box-shadow: 0 5px 15px rgba(227, 30, 36, 0.4);
}

h3 {
  font-size: 22px;
  color: var(--white, #fff);
  margin-bottom: 30px;
  position: relative;
  padding-bottom: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
}

h3::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 50px;
  height: 3px;
  background-color: var(--red, #e31e24);
  border-radius: 2px;
}

ul {
  padding: 0;
  margin: 0;
  list-style: none;
}

ul li {
  margin-bottom: 16px;
}

ul li a {
  color: rgba(255, 255, 255, 0.8);
  font-size: 15px;
  text-decoration: none;
  transition: all 0.3s ease;
  display: inline-block;
}

ul li a:hover {
  color: var(--blue-light, #00a3e0);
  transform: translateX(6px); /* Smooth slide effect */
}

/* Reach Us Section - Improved Alignment */
.reach-list li {
  display: flex;
  align-items: flex-start;
  gap: 15px;
  font-size: 15px;
  opacity: 0.9;
  line-height: 1.6;
}

.reach-list .icon {
  font-size: 18px;
  flex-shrink: 0;
  margin-top: 2px;
}

.reach-list .text {
  color: rgba(255, 255, 255, 0.9);
  transition: color 0.3s ease;
  text-decoration: none;
}

.reach-list a.text:hover {
  color: var(--blue-light, #00a3e0);
}

.iicrc-logo {
  margin-top: 30px;
  background: rgba(255,255,255,0.05);
  display: inline-block;
  padding: 10px;
  border-radius: 8px;
}

.iicrc-logo img {
  height: 65px;
  width: auto;
}

/* Footer Bottom */
.footer-bottom {
  background-color: rgba(0, 0, 0, 0.25);
  padding: 24px 15px; /* Added 15px side padding to prevent touching edges */
  font-size: 14px;
}

.footer-bottom-inner {
  display: flex;
  justify-content: center;
  text-align: center;
}

.footer-bottom p {
  opacity: 0.7;
  letter-spacing: 0.5px;
  margin: 0;
  line-height: 1.6; /* Adds breathing room when text wraps to multiple lines */
  word-wrap: break-word; /* Forces long text to wrap */
}

.footer-bottom a {
  color: var(--blue-light, #00a3e0);
  font-weight: 600;
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-bottom a:hover {
  color: var(--white, #fff);
}

/* Responsiveness */
@media (max-width: 1024px) {
  .footer-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 50px 30px;
  }
  .footer-brand p {
    max-width: 100%;
  }
}

@media (max-width: 768px) {
  .site-footer {
    padding: 60px 0 0;
  }
  
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 45px;
    text-align: center;
  }

  .footer-logo {
    margin: 0 auto 20px;
  }

  h3::after {
    left: 50%;
    transform: translateX(-50%);
  }

  .social-links {
    justify-content: center;
  }

  ul li a:hover {
    transform: translateX(0);
    color: var(--blue-light, #00a3e0);
  }

  .reach-list li {
    justify-content: center;
    text-align: center;
    flex-direction: column;
    align-items: center;
    gap: 8px;
  }

  .reach-list .icon {
    margin-top: 0;
    margin-bottom: 8px;
    font-size: 24px;
  }

  ul li a {
    font-size: 18px;
    padding: 5px 0;
  }

  .reach-list li, .reach-list .text {
    font-size: 18px;
  }

  .reach-list a.text {
    font-size: 20px;
    font-weight: 700;
    display: block;
    margin-top: 5px;
  }

  .footer-bottom {
    padding: 20px 15px;
  }
  
  .footer-bottom p {
    font-size: 13px; /* Slightly smaller text on mobile to fit better */
  }
}
</style>