<template>
    <div class="box">
        <div class="grid-item">{{teamA}}</div>
        <div class="grid-item">{{teamH}}</div> 
        <div class="grid-item">{{time}}</div> 
        <div class="grid-item"></div>
        <div class="grid-item"></div>  
        <div class="grid-item" style= "text-align: right;">
            <button @click="$router.push('/match')"><i class="fa fa-arrow-right" aria-hidden="true"></i></button>
            
        </div> 
    </div>
</template>
<script>
import 'font-awesome/css/font-awesome.min.css'
export default {
    props:{
        teamA: String,   
        teamH: String,
        time: Date
    }
}
</script>
<style>
    .box {
        background-color: white;
        border: 1px solid black;
        padding:10px;
        margin: auto;
        width: 60%;
        display: grid;
        grid-template-columns: auto auto auto;
    }
    .grid-item {
        padding:10px;
        text-align: center;
    }
</style>