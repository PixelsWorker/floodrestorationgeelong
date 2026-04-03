<script setup>
import { ref } from 'vue'

const reviews = ref([
  {
    name: 'Merrissa Lee',
    rating: 5,
    date: '2 weeks ago',
    text: 'Could not be more grateful for the dedication and commitment to our water damaged building. One phone call and within the hr the whole team arrived, non stop for hours on end to ensure the most efficient and high quality restoration was completed, professional and caring.',
    expanded: false
  },
  {
    name: 'Laura Castellanos',
    rating: 5,
    date: 'a month ago',
    text: 'Highly recommend the team. Rang them for a service and they booked the assessment for the following day and also managed to get us booked in for our cleaning early. Communication was excellent.',
    expanded: false
  },
  {
    name: 'Sheridan Stack',
    rating: 5,
    date: 'a month ago',
    text: 'Highly recommend the team at Flood Restoration Geelong. Very professional and friendly service. Best restoration company in Geelong.',
    expanded: false
  },
  {
    name: 'theo pavelis',
    rating: 5,
    date: 'a year ago',
    text: 'We experienced heavy rain on Boxing day 2023 which had our gutters overflowing and heavily flooding our bedroom. Spiro was quick to respond and gave us great advice and helped us with our insurance claim.',
    expanded: false
  },
  {
    name: 'Joshua Todd',
    rating: 5,
    date: '10 months ago',
    text: 'Spiro and his sons did an incredible job. Very knowledgeable and helpful with their advice. Their communication was great and they were on time and worked very hard.',
    expanded: false
  },
  {
    name: 'Daniel Marchiano',
    rating: 5,
    date: '2 years ago',
    text: 'The team at Flood Restoration Geelong were professional, communicative and timely with their service. I would highly recommend them to anyone in Geelong.',
    expanded: false
  },
  {
    name: 'Mina Regue ...',
    rating: 5,
    date: '2 years ago',
    text: 'I highly recommend this company. They assisted my parents after an accidental flooding in their home and were all so professional and caring. They were very thorough and the communication was great.',
    expanded: false
  },
  {
    name: 'Eliza Graves-Brou...',
    rating: 5,
    date: 'a year ago',
    text: 'Spiro & his son did an amazing job after an unfortunate washing machine mishap. They responded to our call immediately and were at our house within 45 minutes.',
    expanded: false
  },
  {
    name: 'Dylan',
    rating: 5,
    date: 'a month ago',
    text: 'We had Spiro and Peter come out to give some advice on a mysterious bathroom leak that was causing us a lot of anguish and raising fears of long-term water damage. They were responsive, professional, and sincere — giving clear information and guiding us toward the right trades when needed.',
    expanded: false
  },
  {
    name: 'Grace Dove',
    rating: 5,
    date: 'a month ago',
    text: "I can't speak highly enough of Spiro and his team at Flood Restoration Geelong. They are incredibly kind, professional and efficient, and show genuine care for the community. Their support of The Outpost has meant so much, and it's clear they go above and beyond because they truly care! Highly recommend them.",
    expanded: false
  },
  {
    name: 'Craig Harvey',
    rating: 5,
    date: '3 months ago',
    text: 'These guys are the absolute best! We had a flooded laundry and they were transparent, punctual, and thorough throughout the entire process. They diagnosed the issue correctly and applied the right restoration methods for long-lasting results, not just quick fixes.',
    expanded: false
  },
  {
    name: 'Timothy Vogrin',
    rating: 5,
    date: '3 months ago',
    text: 'Any property owners that have issues with water damage and mould — use this company. Spiro was friendly, respectful, and professional. The mould remediation process was straightforward, stress-free, and more affordable than expected.',
    expanded: false
  },
  {
    name: 'Kelly Eastgate',
    rating: 5,
    date: '5 months ago',
    text: 'Excellent service and professional team. Jerry and Spiros were incredible from start to finish. They arrived quickly, assessed everything thoroughly, and their communication, drying equipment, and regular follow-ups made the whole process smooth and worry-free.',
    expanded: false
  },
  {
    name: 'Chloe Chanter',
    rating: 5,
    date: '3 months ago',
    text: 'These guys are the best!! Came out on Christmas Eve day to help me with carpet flooding, they talked me through different ways they could help and were so lovely. I would highly recommend them to anyone!',
    expanded: false
  },
  {
    name: 'Sarah Smith',
    rating: 5,
    date: 'a year ago',
    text: 'Spiro and his son were a fantastic duo. They attended the job promptly and expertly assessed what was required — within an hour of the call. Spiro is friendly, a Geelong local, and his service included great recommendations throughout.',
    expanded: false
  },
  {
    name: 'Nick Brockman',
    rating: 5,
    date: 'a year ago',
    text: "Spiro is an absolute gentleman and really looks after you in your time of need. We flooded our house with a burst water connector and Spiro was extremely responsive, honest and great to work with. He did all he could to keep costs down — an ultimate professional…. and oh, he is a spitting image for Will Ferrell. 😊",
    expanded: false
  },

])

const avatarColors = ['#f7931e', '#4285f4', '#34a853', '#ea4335', '#fbbc05', '#0f9d58', '#ab47bc', '#00acc1']

const toggleExpand = (index) => {
  reviews.value[index].expanded = !reviews.value[index].expanded
}
</script>

<template>
  <section class="testimonials">
    <div class="container">
      <div class="section-header">
        <label class="section-label">Google Reviews</label>
        <h2 class="section-title">What People Say About Us</h2>
        <div class="google-summary">
          <span class="rating-num">5.0</span>
          <div class="stars">⭐⭐⭐⭐⭐</div>
          <p>Based on over 100 verified Google reviews</p>
        </div>
      </div>

      <div class="reviews-grid">
        <div v-for="(review, index) in reviews" :key="index" class="review-card" :class="{ 'is-expanded': review.expanded }">
          <div class="card-header">
            <div class="user-info">
              <div class="avatar" :style="{ backgroundColor: avatarColors[index % avatarColors.length] }">
                {{ review.name.charAt(0) }}
              </div>
              <div>
                <div class="name-row">
                  <span class="name">{{ review.name }}</span>
                  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Google" class="g-logo" width="16" loading="lazy" />
                </div>
                <div class="date">{{ review.date }}</div>
              </div>
            </div>
          </div>
          <div class="stars-row">
            <span v-for="n in review.rating" :key="n" class="star">★</span>
          </div>
          <div class="text-content">
            <p :class="{ 'clamp-text': !review.expanded }">{{ review.text }}</p>
            <button v-if="review.text.length > 120" @click="toggleExpand(index)" class="btn-read-more">
              {{ review.expanded ? 'Show Less' : 'Read More' }}
            </button>
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
  gap: 24px;
}

.review-card {
  background: var(--white);
  padding: 24px;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.03);
  display: flex;
  flex-direction: column;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid transparent;
}

.review-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.08);
  border-color: var(--border);
}

.card-header {
  margin-bottom: 15px;
}

.user-info {
  display: flex;
  gap: 12px;
  align-items: center;
}

.avatar {
  width: 42px;
  height: 42px;
  color: var(--white);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 18px;
  box-shadow: inset 0 0 10px rgba(255,255,255,0.2);
}

.name-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.name {
  font-weight: 700;
  font-size: 15px;
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

.text-content {
  flex-grow: 1;
}

.text-content p {
  font-size: 14px;
  line-height: 1.6;
  color: var(--text-mid);
}

.clamp-text {
  display: -webkit-box;
  -webkit-line-clamp: 4;
  line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.btn-read-more {
  background: none;
  border: none;
  color: var(--blue);
  font-size: 12px;
  font-weight: 700;
  padding: 0;
  margin-top: 10px;
  cursor: pointer;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.btn-read-more:hover {
  text-decoration: underline;
  color: var(--navy);
}

@media (max-width: 1200px) {
  .reviews-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 992px) {
  .reviews-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .reviews-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  .testimonials {
    padding: 60px 0;
  }
  .review-card {
    padding: 20px;
  }
  .rating-num {
    font-size: 36px;
  }
}
</style>
