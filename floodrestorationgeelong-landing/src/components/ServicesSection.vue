<script setup>
const services = [
  {
    title: 'Emergency Water Damage Restoration',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2025/10/carpet-cleaning-4-2-1024x768.webp',
    link: 'https://floodrestorationgeelong.au/emergency-water-restoration-geelong'
  },
  {
    title: 'Carpet Water Extraction',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2025/10/Carpet-cleaning-2-1-1-1024x768.webp',
    link: 'https://floodrestorationgeelong.au/carpet-water-extraction-geelong'
  },
  {
    title: 'Carpet Drying',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2025/10/FLood-Restoration-12-1024x768.webp',
    link: 'https://floodrestorationgeelong.au/carpet-drying-geelong'
  },
  {
    title: 'Water Damage Restoration',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2025/10/IMG-20241127-WA0113-1024x768.webp',
    link: 'https://floodrestorationgeelong.au/water-damage-restoration-geelong'
  },
  {
    title: 'Water Damage Repairs',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2026/01/flood-damage-water-extraction-processing-geelong.webp',
    link: 'https://floodrestorationgeelong.au/water-damage-repairs-geelong'
  },
  {
    title: 'Mould Remediation',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2026/01/professional-mould-remediation-geelong.webp',
    link: 'https://floodrestorationgeelong.au/mould-remediation-geelong'
  },
  {
    title: 'Flood Restoration',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2025/10/Flood-Restoration-2-1024x768.webp',
    link: 'https://floodrestorationgeelong.au/flood-damage-restoration-geelong'
  },
  {
    title: 'Burst Pipe Restoration',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2026/01/burst-pipe-water-damage-restoration-geelong.webp',
    link: 'https://floodrestorationgeelong.au/burst-pipes-geelong'
  }
]
</script>

<template>
  <section class="services" id="services">
    <div class="wave-divider top">
      <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
      </svg>
    </div>

    <div class="container relative-z">
      <div class="section-header">
        <label class="section-label">Our Expertise</label>
        <h2 class="section-title">Our Flood Restoration Geelong Services</h2>
        <p class="section-subtitle">Comprehensive water damage recovery solutions for residential and commercial properties in Geelong.</p>
      </div>

      <div class="services-grid">
        <div v-for="(service, index) in services" :key="index" class="service-card">
          <div class="card-image">
            <img 
              :src="service.image" 
              :srcset="`${service.image.replace('-1024x768.webp', '-768x576.webp')} 768w, ${service.image} 1024w`"
              sizes="(max-width: 768px) 100vw, (max-width: 1100px) 33vw, 300px"
              :alt="service.title"
              loading="lazy"
              decoding="async"
              width="800"
              height="600"
            />
            <div class="overlay">
              <a :href="service.link" target="_blank" rel="noopener" class="btn btn-sm btn-primary">View Service</a>
            </div>
          </div>
          <div class="card-body">
            <h3><a :href="service.link" target="_blank" rel="noopener">{{ service.title }}</a></h3>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.services {
  background-color: var(--soft-blue);
  position: relative;
  overflow: visible;
  padding: 100px 0 120px;
}

.relative-z {
  position: relative;
  z-index: 2;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 25px;
}

.service-card {
  background: var(--white);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 119, 204, 0.04);
  transition: var(--transition-fast);
  border: 1px solid rgba(0, 119, 204, 0.05);
}

.service-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 15px 35px rgba(0, 119, 204, 0.1);
  border-color: var(--blue-light);
}

.card-image {
  position: relative;
  height: 220px;
  overflow: hidden;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

.service-card:hover .card-image img {
  transform: scale(1.1);
}

.card-image .overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(11, 37, 69, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: var(--transition-fast);
}

.service-card:hover .overlay {
  opacity: 1;
}

.card-body {
  padding: 24px;
  text-align: center;
}

.card-body h3 {
  font-size: 17px;
  color: var(--navy);
  font-weight: 700;
  line-height: 1.4;
}

.card-body h3 a:hover {
  color: var(--blue);
}

@media (max-width: 1100px) {
  .services-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 992px) {
  .services-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }
  .card-image {
    height: 200px;
  }
}

@media (max-width: 768px) {
  .services {
    padding: 60px 0;
  }
  .section-header {
    margin-bottom: 40px;
  }
}

@media (max-width: 768px) {
  .services-grid {
    grid-template-columns: 1fr;
  }
  .card-image {
    height: 240px;
  }
  .card-body {
    padding: 20px;
  }
  .card-body h3 {
    font-size: 16px;
  }
}

</style>
