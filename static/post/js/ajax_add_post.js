// #####################
// Ajax add post
// #####################
const form_add_post = document.getElementById("form-add-new-post");
const msg = document.getElementById("textarea_id");
const img = document.getElementById("file");
const csrf = document.getElementsByName("csrfmiddlewaretoken");

form_add_post.addEventListener("submit", (e) => {
  e.preventDefault();

  const fd = new FormData();
  fd.append("csrfmiddlewaretoken", csrf[0].value);
  fd.append("message", msg.value);
  fd.append("img", img.files[0]);

  $.ajax({
    type: "POST",
    url: "{% url 'add_post' %}",
    enctype: "multipart/form-data",
    data: fd,
    success: function (response) {
      console.log(response.post_data);
    },
    error: function (error) {
      console.log(error);
    },
    cache: false,
    contentType: false,
    processData: false,
  });

  const previous_container = document.querySelector(".previous-new-add-post");
  const previous_p_img_container = document.querySelector(".previous-post-img");
  const input_img = document.querySelector(".form-input-file");
  const input_text = document.getElementById("textarea_id");
  const p_text = document.getElementById("previous-message");
  const p_img = document.getElementById("previous-post-image");

  input_text.value = "";
  input_img.value = "";
  p_text.textContent = "";
  p_img.setAttribute("src", "");
  previous_p_img_container.classList.add("display-none");
  previous_container.classList.add("display-none");
});

// #####################
// Ajax delete post
// #####################
const btn_del = document.querySelectorAll(".btn-del-post");

let post_id;

btn_del.forEach((element) => {
  element.addEventListener("click", (e) => {
    // console.log(`name: ${e.target.name}`);
    post_id = e.target.id;

    const fd = new FormData();
    fd.append("csrfmiddlewaretoken", csrf[0].value);
    fd.append("post_id", post_id);

    $.ajax({
      type: "POST",
      url: "{% url 'delete_post' %}",
      // enctype: 'multipart/form-data',
      data: fd,
      success: function (response) {
        console.log(response);
      },
      error: function (error) {
        console.log(error);
      },
      cache: false,
      contentType: false,
      processData: false,
    });
    document
      .getElementById("options-container" + post_id)
      .remove("display-none");
  });
});
