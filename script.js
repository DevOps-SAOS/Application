let correctAnswer = null;

function generateExercise(operation) {
  let num1 = Math.floor(Math.random() * 20) + 1;
  let num2 = Math.floor(Math.random() * 20) + 1;

  switch (operation) {
    case 'add':
      correctAnswer = num1 + num2;
      return `${num1} + ${num2} = ?`;

    case 'sub':
      if (num2 > num1) [num1, num2] = [num2, num1];
      correctAnswer = num1 - num2;
      return `${num1} - ${num2} = ?`;

    case 'mul':
      correctAnswer = num1 * num2;
      return `${num1} × ${num2} = ?`;

    case 'div':
      correctAnswer = num1;  // Answer should be integer
      const product = num1 * num2;
      return `${product} ÷ ${num2} = ?`;

    default:
      return '';
  }
}

document.getElementById('generate').addEventListener('click', () => {
  const operation = document.getElementById('operation').value;
  const exerciseText = generateExercise(operation);

  document.getElementById('exercise').textContent = exerciseText;
  document.getElementById('feedback').textContent = '';
  document.getElementById('answer-label').style.display = 'block';
  document.getElementById('check').style.display = 'block';
  document.getElementById('userAnswer').value = '';
});

document.getElementById('check').addEventListener('click', () => {
  const userAnswer = parseFloat(document.getElementById('userAnswer').value);
  const feedback = document.getElementById('feedback');

  if (isNaN(userAnswer)) {
    feedback.textContent = '⚠️ נא להזין מספר';
    feedback.style.color = 'orange';
  } else if (Math.abs(userAnswer - correctAnswer) < 0.0001) {
    feedback.textContent = '✅ תשובה נכונה! כל הכבוד!';
    feedback.style.color = 'green';
  } else {
    feedback.textContent = '❌ לא נכון. נסה שוב';
    feedback.style.color = 'red';
  }
});
