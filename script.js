const judgeData = {
  najeeb: {
    name: "Shaykh Mohamed Najeeb",
    bio: "Mohammed Najeeb has a Bachelors degree in Sharia (Islamic Law) from the esteemed Islamic University of Medinah. He also has a Masters degree and PhD from the College of Quran in the same University. He has Ijazat in the 10 modes of recitation from Sh. Ihab Fikri Haydar, muqri’ in the Prophet’s Masjid, and has studied with many top scholars in Saudi Arabia. Dr. Mohammed has taught Qira’at and Quranic sciences in the Islamic University of Medinah, and in the Prophetic Masjid in Medinah. He currently is an Imam in Sacramento, CA. He teaches with Zidni Islamic Institute.",
    image: "judge1.jpg"
  },
  sharqawy: {
    name: "Shaykh Abdullah Sharqawy",
    bio: "Sh. Abdullah Elsharkawy completed his memorization of the Qur'an at the age of 9 and went on to graduate with a BA from Al-Azhar. He has 11 Ijazaat in different Qira'at, demonstrating his expertise in Quranic recitation. He currently serves as the Imam and Director of the Qur'an Program at the MCYC Mosque in California. He holds a Master’s Degree in Qur’anic Sciences, is an official Judge in National and International Qur’an Competitions (Egypt and Multiple U.S. States), is a member of the electronic Fatwa group, Al-Azhar Alsharif, is a member of the Preaching and Guidance Authority of the Islamic Research Academy, is a member of the Syndicate of the Memorizers and Reciters of the Noble Qur’an, Egypt, and is an Imam and Khatib, Al-Azhar Alsharif.",
    image: "judge2.jpg"
  },
  judge3: {
    name: "Judge 3",
    bio: "A respected hafidh and teacher with deep roots in Quranic education across the U.S.",
    image: "judge3.jpg"
  }
};

function showJudgeCard(id) {
  const card = document.getElementById('judge-card');
  const info = document.getElementById('judge-info');
  const data = judgeData[id];
  if (data) {
    info.innerHTML = `
      <div class="judge-image-wrapper">
        <img src="${data.image}" alt="${data.name}" class="judge-image" />
      </div>
      <h3>${data.name}</h3>
      <p>${data.bio}</p>
    `;
    card.classList.remove('hidden');
  }
}

function closeJudgeCard() {
  document.getElementById('judge-card').classList.add('hidden');
}

document.addEventListener('keydown', function(e) {
  if (e.key === "Escape") {
    closeJudgeCard();
  }
});

document.getElementById('judge-card').addEventListener('click', function (e) {
  if (e.target.id === 'judge-card') {
    closeJudgeCard();
  }
});
