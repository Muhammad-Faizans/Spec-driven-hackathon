import React, { useState } from 'react';
import { useAuth } from './AuthContext';
import './LoginModal.css';

const LoginModal = ({ isOpen, onClose }) => {
  const [isLogin, setIsLogin] = useState(true);
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    fullName: '',
    softwareBackground: '',
    hardwareBackground: '',
    programmingLanguages: '',
    roboticsAiExperience: false
  });
  const [errors, setErrors] = useState({});
  const { login, register } = useAuth();

  if (!isOpen) return null;

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
    
    // Clear error when user starts typing
    if (errors[name]) {
      setErrors(prev => {
        const newErrors = { ...prev };
        delete newErrors[name];
        return newErrors;
      });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Validation
    const newErrors = {};
    if (!formData.email) newErrors.email = 'Email is required';
    if (!formData.password) newErrors.password = 'Password is required';
    if (formData.password.length < 6) newErrors.password = 'Password must be at least 6 characters';
    
    if (!isLogin) {
      if (!formData.fullName) newErrors.fullName = 'Full name is required';
    }
    
    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    if (isLogin) {
      // Login
      const result = await login(formData.email, formData.password);
      if (result.success) {
        onClose();
      } else {
        setErrors({ general: result.error });
      }
    } else {
      // Registration with additional fields
      const userData = {
        email: formData.email,
        password: formData.password,
        full_name: formData.fullName,
        software_background: formData.softwareBackground,
        hardware_background: formData.hardwareBackground,
        programming_languages: formData.programmingLanguages,
        robotics_ai_experience: formData.roboticsAiExperience
      };
      
      const result = await register(userData);
      if (result.success) {
        // Auto-login after registration
        const loginResult = await login(formData.email, formData.password);
        if (loginResult.success) {
          onClose();
        }
      } else {
        setErrors({ general: result.error });
      }
    }
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        <div className="modal-header">
          <h2>{isLogin ? 'Sign In' : 'Sign Up'}</h2>
          <button className="close-btn" onClick={onClose}>×</button>
        </div>
        
        <form onSubmit={handleSubmit} className="auth-form">
          {!isLogin && (
            <div className="form-group">
              <label htmlFor="fullName">Full Name *</label>
              <input
                type="text"
                id="fullName"
                name="fullName"
                value={formData.fullName}
                onChange={handleChange}
                className={errors.fullName ? 'error' : ''}
              />
              {errors.fullName && <span className="error-message">{errors.fullName}</span>}
            </div>
          )}
          
          <div className="form-group">
            <label htmlFor="email">Email *</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className={errors.email ? 'error' : ''}
            />
            {errors.email && <span className="error-message">{errors.email}</span>}
          </div>
          
          <div className="form-group">
            <label htmlFor="password">Password *</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className={errors.password ? 'error' : ''}
            />
            {errors.password && <span className="error-message">{errors.password}</span>}
          </div>
          
          {!isLogin && (
            <>
              <div className="form-group">
                <label htmlFor="softwareBackground">Software Background</label>
                <select
                  id="softwareBackground"
                  name="softwareBackground"
                  value={formData.softwareBackground}
                  onChange={handleChange}
                >
                  <option value="">Select level</option>
                  <option value="beginner">Beginner</option>
                  <option value="intermediate">Intermediate</option>
                  <option value="advanced">Advanced</option>
                </select>
              </div>
              
              <div className="form-group">
                <label htmlFor="hardwareBackground">Hardware Background</label>
                <textarea
                  id="hardwareBackground"
                  name="hardwareBackground"
                  value={formData.hardwareBackground}
                  onChange={handleChange}
                  placeholder="Describe your hardware experience..."
                ></textarea>
              </div>
              
              <div className="form-group">
                <label htmlFor="programmingLanguages">Programming Languages Known</label>
                <input
                  type="text"
                  id="programmingLanguages"
                  name="programmingLanguages"
                  value={formData.programmingLanguages}
                  onChange={handleChange}
                  placeholder="e.g., Python, C++, JavaScript"
                />
              </div>
              
              <div className="form-group checkbox-group">
                <label>
                  <input
                    type="checkbox"
                    name="roboticsAiExperience"
                    checked={formData.roboticsAiExperience}
                    onChange={handleChange}
                  />
                  Robotics / AI Experience (Yes/No)
                </label>
              </div>
            </>
          )}
          
          {errors.general && <div className="error-message general-error">{errors.general}</div>}
          
          <button type="submit" className="submit-btn">
            {isLogin ? 'Sign In' : 'Sign Up'}
          </button>
          
          <div className="switch-form">
            {isLogin ? "Don't have an account? " : "Already have an account? "}
            <button 
              type="button" 
              className="switch-link"
              onClick={() => setIsLogin(!isLogin)}
            >
              {isLogin ? 'Sign Up' : 'Sign In'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginModal;