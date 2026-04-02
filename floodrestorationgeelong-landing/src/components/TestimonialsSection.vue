<script setup>
const reviews = [
  {
    name: 'Merrissa Lee',
    rating: 5,
    text: 'Could not be more grateful for the dedication and commitment to our water damaged building. One phone call and within the hr the whole team arrived, non stop for hours on end to ensure the most efficient and high quality restoration was completed, professional and caring.'
  },
  {
    name: 'Kelly Eastgate',
    rating: 5,
    text: 'Excellent Service and Professional Team. I recently had to deal with unexpected water damage at my property, and Jerry and Spiros were incredible from the start to finish. They arrived quickly, assessed the situation thoroughly, and explained every step of the process.'
  },
  {
    name: 'Spiro',
    rating: 5,
    text: 'Spiro is an absolute gentleman and really looks after you in your time of need. We flooded our house with a burst water connector and Spiro was extremely responsive, honest and great to work with.'
  }
]
</script>

<template>
  <section class="testimonials">
    <div class="container">
      <div class="section-title">
        <h2>What People Say About Us</h2>
        <div class="stars">⭐⭐⭐⭐⭐ 5.0 Google Rating</div>
      </div>

      <div class="reviews-grid">
        <div v-for="(review, index) in reviews" :key="index" class="review-card">
          <div class="rating">
            <span v-for="n in review.rating" :key="n">⭐</span>
          </div>
          <p>"{{ review.text }}"</p>
          <div class="author">
            <div class="avatar">{{ review.name.charAt(0) }}</div>
            <div class="name">{{ review.name }}</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.testimonials {
  background-color: var(--bg-accent);
}

.section-title {
  text-align: center;
  margin-bottom: 50px;
}

.stars {
  color: #ffb400;
  font-weight: 700;
  margin-top: 10px;
}

.reviews-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
}

.review-card {
  background: var(--white);
  padding: 40px;
  border-radius: 12px;
  box-shadow: var(--shadow-main);
  position: relative;
}

.rating {
  margin-bottom: 20px;
  font-size: 14px;
}

p {
  font-style: italic;
  color: var(--text-light);
  line-height: 1.8;
  margin-bottom: 24px;
  font-size: 15px;
}

.author {
  display: flex;
  align-items: center;
  gap: 12px;
  border-top: 1px solid #eee;
  padding-top: 20px;
}

.avatar {
  width: 40px;
  height: 40px;
  background-color: var(--primary-color);
  color: var(--white);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
}

.name {
  font-weight: 600;
  color: var(--secondary-color);
}

@media (max-width: 992px) {
  .reviews-grid {
    grid-template-columns: 1fr;
  }
}
</style>
