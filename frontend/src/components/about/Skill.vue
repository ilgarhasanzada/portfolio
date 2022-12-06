<template>
    <div>
    <svg viewBox="0 0 36 36" class="circular-chart orange">
        <path class="circle-bg"
            d="M18 2.0845
            a 15.9155 15.9155 0 0 1 0 31.831
            a 15.9155 15.9155 0 0 1 0 -31.831"
        />
        <path class="circle"
            :stroke-dasharray="persentage+',100'"
            d="M18 2.0845
            a 15.9155 15.9155 0 0 1 0 31.831
            a 15.9155 15.9155 0 0 1 0 -31.831"
        />
        <text x="18" y="20.35" class="percentage">{{persentage}}%</text>
        </svg><div class="text-light text-center">{{language}}</div>
    </div>
</template>

<script>
export default {
    name:"SkillVue",
    props:{
        language:String,
        persentage:Number
    }
}
</script>

  
<style>

.circular-chart {
  display: block;
  margin: 10px auto;
  max-width: 80%;
  max-height: 130px;
}

.circle-bg {
  fill: none;
  stroke: #2b2a2a;
  stroke-width: 3.8;
}

.circle {
  fill: none;
  stroke-width: 2.8;
  stroke-linecap: round;
  animation: progress 1s ease-out forwards;
}

@keyframes progress {
  0% {
    stroke-dasharray: 0 100;
  }
}

.circular-chart.orange .circle {
  stroke: var(--my-red);
}

.circular-chart.green .circle {
  stroke: #4CC790;
}

.circular-chart.blue .circle {
  stroke: #3c9ee5;
}

.percentage {
  fill: #fff;
  font-family: sans-serif;
  font-size: 0.5em;
  text-anchor: middle;
}
@media screen and (max-width: 991px) {
.circular-chart {
  max-height: 100px;
} 
}
</style>