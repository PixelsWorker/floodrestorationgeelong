<script setup>
const services = [
  {
    title: 'Emergency Water Damage Restoration',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2025/10/carpet-cleaning-4-2-1024x768.webp',
    link: '/emergency-water-restoration-geelong'
  },
  {
    title: 'Carpet Water Extraction',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2025/10/Carpet-cleaning-2-1-1-1024x768.webp',
    link: '/carpet-water-extraction-geelong'
  },
  {
    title: 'Carpet Drying',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2025/10/FLood-Restoration-12-1024x768.webp',
    link: '/carpet-drying-geelong'
  },
  {
    title: 'Water Damage Restoration',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2025/10/IMG-20241127-WA0113-1024x768.webp',
    link: '/water-damage-restoration-geelong'
  },
  {
    title: 'Water Damage Repairs',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2026/01/flood-damage-water-extraction-processing-geelong.webp',
    link: '/water-damage-repairs-geelong'
  },
  {
    title: 'Mould Remediation',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2026/01/professional-mould-remediation-geelong.webp',
    link: '/mould-remediation-geelong'
  },
  {
    title: 'Flood Restoration',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2025/10/Flood-Restoration-2-1024x768.webp',
    link: '/flood-damage-restoration-geelong'
  },
  {
    title: 'Burst Pipe Restoration',
    image: 'https://floodrestorationgeelong.au/wp-content/uploads/2026/01/burst-pipe-water-damage-restoration-geelong.webp',
    link: '/burst-pipes-geelong'
  }
]
</script>

<template>
  <section class="services" id="services">
    <div class="container">
      <div class="section-title">
        <h2>Our Flood Restoration Geelong Services</h2>
        <div class="divider"></div>
      </div>

      <div class="services-grid">
        <div v-for="(service, index) in services" :key="index" class="service-card">
          <div class="card-image">
            <img :src="service.image" :alt="service.title" />
            <div class="overlay">
              <a :href="service.link" class="btn btn-sm">View Service</a>
            </div>
          </div>
          <div class="card-body">
            <h3><a :href="service.link">{{ service.title }}</a></h3>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.services {
  background-color: var(--white);
}

.section-title {
  text-align: center;
  margin-bottom: 50px;
}

.section-title h2 {
  font-size: 36px;
  color: var(--secondary-color);
  margin-bottom: 15px;
}

.divider {
  width: 80px;
  height: 4px;
  background-color: var(--primary-color);
  margin: 0 auto;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
}

.service-card {
  background: var(--white);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0,0,0,0.05);
  transition: var(--transition-fast);
}

.service-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 30px rgba(0,0,0,0.1);
}

.card-image {
  position: relative;
  height: 200px;
  overflow: hidden;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
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
  background: rgba(0, 119, 204, 0.6);
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
  padding: 20px;
  text-align: center;
}

.card-body h3 {
  font-size: 18px;
  color: var(--secondary-color);
}

.card-body h3 a:hover {
  color: var(--primary-color);
}

.btn-sm {
  padding: 8px 20px;
  font-size: 14px;
}

@media (max-width: 1200px) {
  .services-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 576px) {
  .services-grid {
    grid-template-columns: 1fr;
  }
}
</style>
