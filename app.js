// Application State
const state = {
  currentPage: 'home',
  userType: 'student',
  messages: [],
  financialData: {
    income: 5000,
    expenses: 3500,
    savingsRate: 20.0,
    debtRatio: 10.0,
    spending: {
      housing: 1200,
      food: 600,
      transportation: 400,
      entertainment: 300,
      healthcare: 200,
      other: 200
    },
    debt: 500
  }
};

// Chart instances
let spendingChart = null;
let overviewChart = null;

// Initialize Application
document.addEventListener('DOMContentLoaded', () => {
  initializeNavigation();
  initializeChatFeatures();
  initializeAnalytics();
  initializeFAQ();
});

// Navigation
function initializeNavigation() {
  const navItems = document.querySelectorAll('.nav-item');
  const pages = document.querySelectorAll('.page');

  navItems.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const targetPage = item.dataset.page;
      navigateToPage(targetPage);
    });
  });

  // Handle CTA buttons
  const navButtons = document.querySelectorAll('[data-navigate]');
  navButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetPage = btn.dataset.navigate;
      navigateToPage(targetPage);
    });
  });
}

function navigateToPage(pageName) {
  // Update state
  state.currentPage = pageName;

  // Update active nav item
  document.querySelectorAll('.nav-item').forEach(item => {
    item.classList.remove('active');
    if (item.dataset.page === pageName) {
      item.classList.add('active');
    }
  });

  // Update active page
  document.querySelectorAll('.page').forEach(page => {
    page.classList.remove('active');
  });
  document.getElementById(`${pageName}-page`).classList.add('active');

  // Initialize charts if navigating to analytics
  if (pageName === 'analytics') {
    setTimeout(() => {
      initializeCharts();
    }, 100);
  }
}

// Chat Features
function initializeChatFeatures() {
  // User type selection
  const userTypeRadios = document.querySelectorAll('input[name="userType"]');
  userTypeRadios.forEach(radio => {
    radio.addEventListener('change', (e) => {
      state.userType = e.target.value;
      document.getElementById('user-mode').textContent = 
        e.target.value === 'student' ? 'Student Mode' : 'Professional Mode';
    });
  });

  // Clear chat button
  document.querySelector('.btn-clear').addEventListener('click', () => {
    clearChat();
  });

  // Quick prompts
  const promptCards = document.querySelectorAll('.prompt-card');
  promptCards.forEach(card => {
    card.addEventListener('click', () => {
      const promptText = card.textContent;
      document.getElementById('chat-input').value = promptText;
      sendMessage();
    });
  });

  // Send message
  document.getElementById('send-btn').addEventListener('click', sendMessage);
  document.getElementById('chat-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      sendMessage();
    }
  });
}

function sendMessage() {
  const input = document.getElementById('chat-input');
  const message = input.value.trim();
  
  if (!message) return;

  // Add user message
  addMessageToChat('user', message);
  input.value = '';

  // Simulate AI response
  setTimeout(() => {
    const response = generateAIResponse(message);
    addMessageToChat('assistant', response);
  }, 1000);
}

function addMessageToChat(role, content) {
  const messagesContainer = document.getElementById('chat-messages');
  
  // Remove welcome card if it exists
  const welcomeCard = messagesContainer.querySelector('.welcome-card');
  if (welcomeCard) {
    welcomeCard.remove();
  }

  const messageDiv = document.createElement('div');
  messageDiv.className = `message ${role}`;
  
  const contentDiv = document.createElement('div');
  contentDiv.className = 'message-content';
  contentDiv.textContent = content;
  
  messageDiv.appendChild(contentDiv);
  messagesContainer.appendChild(messageDiv);
  
  // Scroll to bottom
  messagesContainer.scrollTop = messagesContainer.scrollHeight;
  
  // Save to state
  state.messages.push({ role, content });
}

function generateAIResponse(userMessage) {
  const lowerMessage = userMessage.toLowerCase();
  
  if (lowerMessage.includes('budget')) {
    return `As a ${state.userType}, I recommend the 50/30/20 budgeting rule: 50% for needs, 30% for wants, and 20% for savings and debt repayment. Based on your profile, let's create a customized budget plan that aligns with your financial goals.`;
  } else if (lowerMessage.includes('invest')) {
    return `For ${state.userType}s, I suggest starting with low-cost index funds and ETFs. Consider opening a Roth IRA or 401(k) if available. Start with small, consistent investments and gradually increase as you become more comfortable.`;
  } else if (lowerMessage.includes('expense') || lowerMessage.includes('reduce')) {
    return `Let's analyze your spending patterns. Common areas to reduce expenses include: dining out, subscription services, and impulse purchases. I recommend tracking your expenses for a month and identifying non-essential spending.`;
  } else if (lowerMessage.includes('tax')) {
    return `Key tax deductions you might be missing: student loan interest, retirement contributions, education expenses, and home office deductions if applicable. Consult with a tax professional for personalized advice.`;
  } else if (lowerMessage.includes('debt')) {
    return `The debt avalanche method suggests paying off high-interest debt first. However, if debt is low-interest and you have no emergency fund, consider building 3-6 months of expenses first. Balance is key!`;
  } else if (lowerMessage.includes('emergency')) {
    return `Aim for 3-6 months of living expenses in your emergency fund. For ${state.userType}s, start with $1,000 and build from there. Keep it in a high-yield savings account for easy access.`;
  } else {
    return `I'm here to help with all your financial questions! I can provide guidance on budgeting, investing, saving, debt management, and more. Feel free to ask me anything specific about your financial situation.`;
  }
}

function clearChat() {
  const messagesContainer = document.getElementById('chat-messages');
  messagesContainer.innerHTML = `
    <div class="welcome-card">
      <div class="welcome-icon">
        <i class="fas fa-comments"></i>
      </div>
      <h3>Welcome to FinanceAI</h3>
      <p>I'm your personal finance assistant. Ask me anything about budgeting, investing, saving, or managing your finances!</p>
    </div>
  `;
  state.messages = [];
}

// Analytics
function initializeAnalytics() {
  const form = document.getElementById('financial-form');
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    updateFinancialData();
  });
}

function initializeCharts() {
  createSpendingChart();
  createOverviewChart();
}

function createSpendingChart() {
  const ctx = document.getElementById('spending-chart');
  if (!ctx) return;

  if (spendingChart) {
    spendingChart.destroy();
  }

  const { spending } = state.financialData;
  
  spendingChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Housing', 'Food', 'Transportation', 'Entertainment', 'Healthcare', 'Other'],
      datasets: [{
        data: [
          spending.housing,
          spending.food,
          spending.transportation,
          spending.entertainment,
          spending.healthcare,
          spending.other
        ],
        backgroundColor: [
          '#10B981',
          '#3B82F6',
          '#F59E0B',
          '#EC4899',
          '#14B8A6',
          '#6B7280'
        ],
        borderWidth: 2,
        borderColor: '#fff'
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            padding: 15,
            font: {
              size: 12
            }
          }
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              const label = context.label || '';
              const value = context.parsed || 0;
              return `${label}: $${value.toLocaleString()}`;
            }
          }
        }
      }
    }
  });
}

function createOverviewChart() {
  const ctx = document.getElementById('overview-chart');
  if (!ctx) return;

  if (overviewChart) {
    overviewChart.destroy();
  }

  const { income, expenses, debt } = state.financialData;
  const savings = income - expenses;

  overviewChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Income', 'Expenses', 'Savings', 'Debt'],
      datasets: [{
        label: 'Amount ($)',
        data: [income, expenses, savings, debt],
        backgroundColor: [
          '#10B981',
          '#3B82F6',
          '#8B5CF6',
          '#EF4444'
        ],
        borderRadius: 8,
        borderWidth: 0
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      indexAxis: 'y',
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              const value = context.parsed.x || 0;
              return `$${value.toLocaleString()}`;
            }
          }
        }
      },
      scales: {
        x: {
          beginAtZero: true,
          ticks: {
            callback: function(value) {
              return '$' + value.toLocaleString();
            }
          }
        }
      }
    }
  });
}

function updateFinancialData() {
  // Get form values
  const income = parseFloat(document.getElementById('income-input').value);
  const housing = parseFloat(document.getElementById('housing-input').value);
  const food = parseFloat(document.getElementById('food-input').value);
  const transportation = parseFloat(document.getElementById('transportation-input').value);
  const entertainment = parseFloat(document.getElementById('entertainment-input').value);
  const healthcare = parseFloat(document.getElementById('healthcare-input').value);
  const other = parseFloat(document.getElementById('other-input').value);
  const debt = parseFloat(document.getElementById('debt-input').value);

  // Calculate totals
  const totalExpenses = housing + food + transportation + entertainment + healthcare + other;
  const savings = income - totalExpenses;
  const savingsRate = ((savings / income) * 100).toFixed(1);
  const debtRatio = ((debt / income) * 100).toFixed(1);

  // Update state
  state.financialData = {
    income,
    expenses: totalExpenses,
    savingsRate: parseFloat(savingsRate),
    debtRatio: parseFloat(debtRatio),
    spending: {
      housing,
      food,
      transportation,
      entertainment,
      healthcare,
      other
    },
    debt
  };

  // Update display
  document.getElementById('income-display').textContent = income.toLocaleString();
  document.getElementById('expenses-display').textContent = totalExpenses.toLocaleString();
  document.getElementById('savings-rate-display').textContent = savingsRate;
  document.getElementById('debt-ratio-display').textContent = debtRatio;

  // Update charts
  createSpendingChart();
  createOverviewChart();

  // Show success message
  alert('Financial data updated successfully!');
}

// FAQ
function initializeFAQ() {
  const faqQuestions = document.querySelectorAll('.faq-question');
  faqQuestions.forEach(question => {
    question.addEventListener('click', () => {
      const faqItem = question.parentElement;
      const isActive = faqItem.classList.contains('active');
      
      // Close all FAQ items
      document.querySelectorAll('.faq-item').forEach(item => {
        item.classList.remove('active');
      });
      
      // Toggle current item
      if (!isActive) {
        faqItem.classList.add('active');
      }
    });
  });
}

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});