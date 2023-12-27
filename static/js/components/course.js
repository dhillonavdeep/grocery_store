// components/course.js
const Course = Vue.component("course", {
    props: ['id'],  // Define id as a prop
  
    template: `
      <div>
        <h2>Course Page</h2>
        <p>This is course page for: {{ id }}</p>
      </div>
    `,
  });
  
  export default Course;
  