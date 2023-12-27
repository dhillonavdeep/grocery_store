import router from "./router.js";
document.addEventListener('DOMContentLoaded', function () {
    const app = new Vue({
        el: '#app',
        router: router,
        data: {
            message: "Hello World",
            flag : true
        },
        methods: {},
        mounted:{}
        });
});

