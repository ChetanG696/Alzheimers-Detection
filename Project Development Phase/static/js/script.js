const selectImage = document.querySelector('.select-image');
const inputFile = document.querySelector('#file');
const imgArea = document.querySelector('.img-area');

selectImage.addEventListener('click', function () {
	inputFile.click();
})

inputFile.addEventListener('change', function () {
	const image = this.files[0]
	if(image.size < 2000000) {
		const reader = new FileReader();
		reader.onload = ()=> {
			const allImg = imgArea.querySelectorAll('img');
			allImg.forEach(item=> item.remove());
			const imgUrl = reader.result;
			const img = document.createElement('img');
			img.src = imgUrl;
			imgArea.appendChild(img);
			imgArea.classList.add('active');
			imgArea.dataset.img = image.name;
		}
		reader.readAsDataURL(image);
	} else {
		alert("Image size more than 2MB");
	}
})
$('#btn-predict').click(function () {
	var form_data = new FormData($('#upload-file')[0]);

	// Show loading animation
	$(this).hide();
	$('.loader').show();

	// Make prediction by calling api /predict
	$.ajax({
		type: 'POST',
		url: '/predict',
		data: form_data,
		contentType: false,
		cache: false,
		processData: false,
		async: true,
		success: function (data) {
			// Get and display the result
			$('.loader').hide();
			$('#result').fadeIn(600);
			$('#result').text(' Result:  ' + data);
			console.log('Success!');
		},
	});
})