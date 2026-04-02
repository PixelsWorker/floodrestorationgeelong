<script setup>
const reviews = [
  {
    name: 'Merrissa Lee',
    rating: 5,
    date: '2 weeks ago',
    text: 'Could not be more grateful for the dedication and commitment to our water damaged building. One phone call and within the hr the whole team arrived, non stop for hours on end to ensure the most efficient and high quality restoration was completed, professional and caring.'
  },
  {
    name: 'Laura Castellanos',
    rating: 5,
    date: 'a month ago',
    text: 'Highly recommend the team. Rang them for a service and they booked the assessment for the following day and also managed to get us booked in for our cleaning early. Communication was excellent.'
  },
  {
    name: 'Sheridan Stack',
    rating: 5,
    date: 'a month ago',
    text: 'Highly recommend the team at Flood Restoration Geelong. Very professional and friendly service. Best restoration company in Geelong.'
  },
  {
    name: 'theo pavelis',
    rating: 5,
    date: 'a year ago',
    text: 'We experienced heavy rain on Boxing day 2023 which had our gutters overflowing and heavily flooding our bedroom. Spiro was quick to respond and gave us great advice and helped us with our insurance claim.'
  },
  {
    name: 'Joshua Todd',
    rating: 5,
    date: '10 month ago',
    text: 'Spiro and his sons did an incredible job. Very knowledgeable and helpful with their advice. Their communication was great and they were on time and worked very hard.'
  },
  {
    name: 'Daniel Marchiano',
    rating: 5,
    date: '2 years ago',
    text: 'The team at Flood Restoration Geelong were professional, communicative and timely with their service. I would highly recommend them to anyone in Geelong.'
  },
  {
    name: 'Mina Regue ...',
    rating: 5,
    date: '2 years ago',
    text: 'I highly recommend this company. They assisted my parents after an accidental flooding in their home and were all so professional and caring. They were very thorough and the communication was great.'
  },
  {
    name: 'Eliza Graves-Brou...',
    rating: 5,
    date: 'a year ago',
    text: 'Spiro & his son did an amazing job after an unfortunate washing machine mishap. They responded to our call immediately and were at our house within 45 minutes.'
  }
]
</script>

<template>
  <section class="testimonials">
    <div class="container">
      <div class="section-header">
        <label class="section-label">Google Reviews</label>
        <h2 class="section-title">What People Says About Us</h2>
        <div class="google-summary">
          <span class="rating-num">5.0</span>
          <div class="stars">⭐⭐⭐⭐⭐</div>
          <p>Based on over 100 verified Google reviews</p>
        </div>
      </div>

      <div class="reviews-grid">
        <div v-for="(review, index) in reviews" :key="index" class="review-card">
          <div class="card-header">
            <div class="user-info">
              <div class="avatar">{{ review.name.charAt(0) }}</div>
              <div>
                <div class="name-row">
                  <span class="name">{{ review.name }}</span>
                  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Google" class="g-logo" width="16" />
                </div>
                <div class="date">{{ review.date }}</div>
              </div>
            </div>
          </div>
          <div class="stars-row">
            <span v-for="n in review.rating" :key="n" class="star">★</span>
          </div>
          <div class="text-content">
            <p>{{ review.text }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.testimonials {
  background-color: var(--bg-accent);
  padding: 100px 0;
}

.google-summary {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  margin-bottom: 20px;
}

.rating-num {
  font-size: 42px;
  font-weight: 800;
  color: var(--navy);
}

.google-summary p {
  font-size: 14px;
  color: var(--text-light);
  font-weight: 500;
}

.reviews-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.review-card {
  background: var(--white);
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.03);
  display: flex;
  flex-direction: column;
  transition: var(--transition-fast);
}

.review-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.06);
}

.card-header {
  margin-bottom: 12px;
}

.user-info {
  display: flex;
  gap: 12px;
  align-items: center;
}

.avatar {
  width: 38px;
  height: 38px;
  background-color: #f7931e; /* Google default orange */
  color: var(--white);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 16px;
}

.review-card:nth-child(even) .avatar { background-color: #4285f4; } /* Blue */
.review-card:nth-child(3n) .avatar { background-color: #34a853; } /* Green */
.review-card:nth-child(4n) .avatar { background-color: #ea4335; } /* Red */

.name-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.name {
  font-weight: 700;
  font-size: 14px;
  color: var(--navy);
}

.date {
  font-size: 12px;
  color: var(--text-light);
  margin-top: 2px;
}

.stars-row {
  color: #fbbc05;
  font-size: 18px;
  margin-bottom: 12px;
}

.text-content p {
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--text-mid);
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

@media (max-width: 1200px) {
  .reviews-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .reviews-grid {
    grid-template-columns: 1fr;
    gap: 15px;
  }
  .testimonials {
    padding: 60px 0;
  }
}
</style>
