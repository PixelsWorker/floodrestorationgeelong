<script setup>
const videos = [
  {
    id: '3MpcsgzQGE0',
    title: 'Flood Restoration in Office',
  },
  {
    id: 'ub6Bk-nlje8',
    title: 'Water Damage Restoration',
  },
  {
    id: 'ZOd4APGKdH0',
    title: 'Flood Damage Restoration',
  },
  {
    id: 'p2jKh8yj160',
    title: 'Emergency Water Damage',
  }
]
</script>

<template>
  <section class="video-showcase">
    <div class="container">
      <div class="section-header">
        <label class="section-label">Video Gallery</label>
        <h2 class="section-title">See Our Restoration Team in Action</h2>
        <p class="section-subtitle">Real results from real flood emergencies across Geelong properties.</p>
      </div>

      <div class="video-grid">
        <div v-for="video in videos" :key="video.id" class="video-card">
          <div class="video-wrapper">
            <iframe 
              :src="`https://www.youtube-nocookie.com/embed/${video.id}`" 
              title="YouTube video player" 
              frameborder="0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen
            ></iframe>
          </div>
          <div class="video-info">
            <h3>{{ video.title }}</h3>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.video-showcase {
  background-color: var(--white);
}

.video-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
}

.video-card {
  background: var(--white);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow-card);
  transition: var(--transition-fast);
}

.video-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-main);
}

.video-wrapper {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
  height: 0;
  overflow: hidden;
}

.video-wrapper iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.video-info {
  padding: 20px;
  text-align: center;
}

.video-info h3 {
  font-size: 18px;
  color: var(--navy);
}

@media (max-width: 768px) {
  .video-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  .video-showcase {
    padding: 60px 0;
  }
}
</style>
