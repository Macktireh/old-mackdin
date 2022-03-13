const previous_container = document.querySelector(".previous-post-container");
const previous_img_profile = document.querySelector(
  ".new-add-post-left-container > img"
);
const input_text = document.getElementById("message");
const input_img = document.querySelector(".form-input-file");

const path_img = previous_img_profile.src;
let val;

// console.log(previous_container);

// input_img.addEventListener("change", (e) => {
//   console.log(e);
//   console.log(e.target);
//   console.log(e.target.value);
// });

input_text.addEventListener("input", (e) => {
  let val = e.target.value;
  console.log(val);
  if (val.length >= 1) {
    previous_container.classList.add("test1");
  } else {
    previous_container.classList.remove("test1");
  }
});
