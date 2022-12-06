<template>
  <div class="text-light d-flex">
        <div class="d-flex flex-column align-items-center">
            <div class="edu-icon bg-red rounded-circle d-flex justify-content-center align-items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M20 12.875v5.068c0 2.754-5.789 4.057-9 4.057-3.052 0-9-1.392-9-4.057v-6.294l9 4.863 9-3.637zm-8.083-10.875l-12.917 5.75 12 6.5 11-4.417v7.167h2v-8.25l-12.083-6.75zm13.083 20h-4c.578-1 1-2.5 1-4h2c0 1.516.391 2.859 1 4z"/></svg></div>
            <div class="line bg-gray h-100"></div>
        </div>
        <div class="ms-4">   
            <div><span class="bg-gray rounded px-2"><small>2009 - 2022</small></span></div>
            <div class="my-2">MASTER DEGREE - <small>KIEV UNIVERSITY</small></div>
            <div class="text-secondary">COMPUTER SCIENCE</div>
        </div>
    </div>
</template>

<script>
export default {
    name:'EducationItem'
}
</script>

<style>
.edu-icon{
  width: 40px;
  height: 70px;
}
.line{
  width: 1px;
  height: 20px;
}
</style>