document.getElementById('streak').addEventListener('click', () => {
  let streak = localStorage.getItem('focusStreak') || 0;
  alert(`🔥 Your current Focus Streak: ${streak} days!`);
});
