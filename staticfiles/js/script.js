
document.addEventListener('DOMContentLoaded', () => {
    // Handle comment form submission
    const commentForms = document.querySelectorAll('form.comment-form');
    commentForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault(); 

            const formData = new FormData(form);
            const url = form.action;

            fetch(url, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'), 
                },
            })
            .then(response => response.json())
            .then(data => {
                // Handle success
                if (data.success) {
                    addCommentToDOM(data.comment);
                    form.reset(); 
                } else {
                    alert('Failed to add comment: ' + data.message);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });

    // Handle upvote and downvote buttons
    const upvoteButtons = document.querySelectorAll('.btn-upvote');
    const downvoteButtons = document.querySelectorAll('.btn-downvote');

    upvoteButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            handleVote(button, 'upvote');
        });
    });

    downvoteButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            handleVote(button, 'downvote');
        });
    });

    function handleVote(button, voteType) {
        const recipeId = button.dataset.recipeId;
        const url = button.closest('form').action; 

        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ voteType, recipeId }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Update vote count in the DOM
                const voteCount = button.querySelector('.vote-count');
                if (voteType === 'upvote') {
                    voteCount.textContent = data.newUpvoteCount; 
                } else {
                    voteCount.textContent = data.newDownvoteCount; 
                }
            } else {
                alert('Failed to cast vote: ' + data.message);
            }
        })
        .catch(error => console.error('Error:', error));
    }

    // Helper function to add a new comment to the DOM
    function addCommentToDOM(comment) {
        const commentList = document.querySelector('.comment-list');
        const commentItem = document.createElement('li');
        commentItem.classList.add('media', 'my-4');
        commentItem.innerHTML = `
            <div class="media-body">
                <h5 class="mt-0 mb-1">${comment.author}</h5>
                <p>${comment.content}</p>
                <small class="text-muted">${new Date(comment.created_at).toLocaleString()}</small>
            </div>
        `;
        commentList.appendChild(commentItem);
    }

    // Function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
