<script setup>
const steps = [
  {
    title: '1. Detailed Inspection and Damage Assessment',
    content: 'Every successful restoration begins with a comprehensive inspection. Our technicians assess the full extent of the flood or water damage, identify hidden moisture, and create a customised restoration plan tailored to your property.',
    tip: 'Take photos before we arrive — it helps with documentation and insurance claims.'
  },
  {
    title: '2. Fast and Efficient Water Removal',
    content: 'The next critical stage is water extraction. Using high-powered truck-mounted equipment, we remove standing water quickly and efficiently. This rapid response reduces further damage to floors, walls, and furniture.',
    tip: null
  },
  {
    title: '3. Advanced Drying and Dehumidification',
    content: 'Once the visible water is gone, we move on to thorough drying and dehumidification. Even when surfaces appear dry, moisture often lingers deep within walls, floors, and ceilings.',
    tip: null
  },
  {
    title: '4. Cleaning, Sanitising & Mould Prevention',
    content: 'After drying, we clean and sanitise every affected surface, restoring hygiene and freshness to your property. Our team disinfects walls, flooring, and furniture using eco-friendly antimicrobial cleaning solutions.',
    tip: null
  },
  {
    title: '5. Final Restoration & Quality Check',
    content: 'In the final stage, we complete a thorough property restoration, ensuring everything is safe, clean, and restored to pre-damage condition.',
    tip: null
  }
]
</script>

<template>
  <section class="how-it-works">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Our IICRC-Certified Flood Restoration Process:</h2>
        <h3 class="process-subtitle">A Step-by-Step Guide to Recovery</h3>
        <p class="section-subtitle">We value transparency. Knowing what to expect can greatly lessen stress during a crisis.</p>
      </div>

      <div class="process-grid">
        <div v-for="(step, index) in steps" :key="index" class="step-card">
          <div class="step-num">{{ index + 1 }}</div>
          <div class="step-content">
            <h4>{{ step.title }}</h4>
            <p>{{ step.content }}</p>
            <div v-if="step.tip" class="step-tip">
              <strong>Pro tip:</strong> {{ step.tip }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.how-it-works {
  background-color: var(--white);
  padding: 100px 0;
}

.process-subtitle {
  font-size: 28px;
  color: var(--blue);
  margin-bottom: 20px;
  font-weight: 700;
}

.process-grid {
  max-width: 1000px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.step-card {
  display: flex;
  gap: 30px;
  background: var(--bg-accent);
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 119, 204, 0.05);
  transition: var(--transition-fast);
  align-items: flex-start;
}

.step-card:hover {
  transform: translateX(10px);
  background: var(--white);
  box-shadow: var(--shadow-main);
}

.step-num {
  flex-shrink: 0;
  width: 50px;
  height: 50px;
  background: var(--blue);
  color: var(--white);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  font-weight: 800;
  margin-top: -5px;
}

.step-content h4 {
  font-size: 20px;
  color: var(--navy);
  margin-bottom: 12px;
}

.step-content p {
  color: var(--text-mid);
  line-height: 1.8;
  font-size: 15px;
}

.step-tip {
  margin-top: 20px;
  padding: 12px 18px;
  background: rgba(0, 119, 204, 0.08);
  border-radius: 6px;
  font-size: 14px;
  color: var(--blue);
}

@media (max-width: 768px) {
  .step-card {
    flex-direction: column;
    padding: 30px;
  }
  
  .step-num {
    margin-top: 0;
  }
}
</style>
