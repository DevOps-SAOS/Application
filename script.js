function generatePassword(length, useLower, useUpper, useNumbers, useSymbols) {
  const lowercase = 'abcdefghijklmnopqrstuvwxyz';
  const uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const numbers = '0123456789';
  const symbols = '!@#$%^&*()_+[]{}<>?,./';

  let chars = '';
  if (useLower) chars += lowercase;
  if (useUpper) chars += uppercase;
  if (useNumbers) chars += numbers;
  if (useSymbols) chars += symbols;

  if (chars === '') return '⚠️ בחר לפחות סוג אחד של תווים';

  let password = '';
  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * chars.length);
    password += chars[randomIndex];
  }

  return password;
}

document.getElementById('generate').addEventListener('click', () => {
  const length = parseInt(document.getElementById('length').value, 10);
  const useLower = document.getElementById('lowercase').checked;
  const useUpper = document.getElementById('uppercase').checked;
  const useNumbers = document.getElementById('numbers').checked;
  const useSymbols = document.getElementById('symbols').checked;

  const password = generatePassword(length, useLower, useUpper, useNumbers, useSymbols);
  const result = document.getElementById('result');
  const copyButton = document.getElementById('copy');

  result.textContent = password;

  if (!password.startsWith('⚠️')) {
    copyButton.style.display = 'block';
    copyButton.textContent = '📋 העתק ללוח';
    copyButton.onclick = () => {
      navigator.clipboard.writeText(password).then(() => {
        copyButton.textContent = '✅ הועתק!';
        setTimeout(() => {
          copyButton.textContent = '📋 העתק ללוח';
        }, 2000);
      });
    };
  } else {
    copyButton.style.display = 'none';
  }
});
