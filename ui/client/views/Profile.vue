<template>
    <div :key=$route.params.id class="page-container">
        <div class="box">
            <h1 class="title is-1">Howdy {{ $store.state.username }}!</h1>
            <hr>
            <div class="subtitle">Welcome to the first page!</div>
        </div>
    </div>
</template>
