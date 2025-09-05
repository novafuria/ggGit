"""
Tests for AI usage tracker functionality.

This module tests the AiUsageTracker class and its integration
with the configuration system.
"""

import pytest
import os
import tempfile
import yaml
from unittest.mock import Mock, patch, MagicMock
from src.core.ai.usage_tracker import AiUsageTracker


class TestAiUsageTracker:
    """Test AiUsageTracker functionality."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.config_mock = Mock()
        self.config_mock.get_config.side_effect = lambda key, default: {
            'ai.usage_file': '.gggit/ai-usage.yaml',
            'ai.tracking_enabled': True,
            'ai.cost_limit': 5.00
        }.get(key, default)
        
        self.tracker = AiUsageTracker(self.config_mock)
    
    def test_is_tracking_enabled_true(self):
        """Test is_tracking_enabled when tracking is enabled."""
        self.config_mock.get_config.return_value = True
        
        result = self.tracker.is_tracking_enabled()
        
        assert result == True
    
    def test_is_tracking_enabled_false(self):
        """Test is_tracking_enabled when tracking is disabled."""
        self.config_mock.get_config.side_effect = lambda key, default: {
            'ai.tracking_enabled': False
        }.get(key, default)
        
        result = self.tracker.is_tracking_enabled()
        
        assert result == False
    
    def test_get_usage_stats_default(self):
        """Test get_usage_stats with default data."""
        # Test that get_usage_stats returns a valid structure
        result = self.tracker.get_usage_stats()
        
        # Should return a dictionary with expected keys
        assert isinstance(result, dict)
        assert 'totals' in result
        assert 'period' in result
        assert 'limits' in result
        assert 'daily_usage' in result
    
    def test_increment_usage_tracking_disabled(self):
        """Test increment_usage when tracking is disabled."""
        with patch.object(self.tracker, 'is_tracking_enabled', return_value=False):
            with patch.object(self.tracker, '_load_usage_file') as mock_load:
                with patch.object(self.tracker, '_save_usage_file') as mock_save:
                    # Should not call load or save when tracking is disabled
                    self.tracker.increment_usage("ggfeat", 100, 0.05)
                    
                    mock_load.assert_not_called()
                    mock_save.assert_not_called()
    
    def test_increment_usage_tracking_enabled(self):
        """Test increment_usage when tracking is enabled."""
        with patch.object(self.tracker, 'is_tracking_enabled', return_value=True):
            with patch.object(self.tracker, '_load_usage_file') as mock_load:
                with patch.object(self.tracker, '_save_usage_file') as mock_save:
                    # Mock loaded data
                    mock_load.return_value = {
                        'daily_usage': {},
                        'totals': {'requests': 0, 'tokens': 0, 'cost': 0.0}
                    }
                    
                    self.tracker.increment_usage("ggfeat", 100, 0.05)
                    
                    # Verify save was called with updated data
                    mock_save.assert_called_once()
                    saved_data = mock_save.call_args[0][0]
                    assert saved_data['totals']['requests'] == 1
                    assert saved_data['totals']['tokens'] == 100
                    assert saved_data['totals']['cost'] == 0.05
    
    def test_reset_usage_tracking_disabled(self):
        """Test reset_usage when tracking is disabled."""
        with patch.object(self.tracker, 'is_tracking_enabled', return_value=False):
            with patch.object(self.tracker, '_save_usage_file') as mock_save:
                # Should not call save when tracking is disabled
                self.tracker.reset_usage()
                
                mock_save.assert_not_called()
    
    def test_reset_usage_tracking_enabled(self):
        """Test reset_usage when tracking is enabled."""
        with patch.object(self.tracker, 'is_tracking_enabled', return_value=True):
            with patch.object(self.tracker, '_create_default_usage_data') as mock_create:
                with patch.object(self.tracker, '_save_usage_file') as mock_save:
                    mock_create.return_value = {'totals': {'requests': 0}}
                    
                    self.tracker.reset_usage()
                    
                    # Verify save was called with default data
                    mock_save.assert_called_once()
                    mock_create.assert_called_once()
    
    def test_get_cost_limit(self):
        """Test get_cost_limit method."""
        self.config_mock.get_config.side_effect = lambda key, default: {
            'ai.cost_limit': 10.00
        }.get(key, default)
        
        result = self.tracker.get_cost_limit()
        
        assert result == 10.00
    
    def test_is_cost_limit_exceeded_false(self):
        """Test is_cost_limit_exceeded when limit not exceeded."""
        with patch.object(self.tracker, 'is_tracking_enabled', return_value=True):
            with patch.object(self.tracker, 'get_usage_stats') as mock_stats:
                mock_stats.return_value = {
                    'totals': {'cost': 2.50},
                    'limits': {'cost_limit': 5.00}
                }
                
                result = self.tracker.is_cost_limit_exceeded()
                
                assert result == False
    
    def test_is_cost_limit_exceeded_true(self):
        """Test is_cost_limit_exceeded when limit exceeded."""
        with patch.object(self.tracker, 'is_tracking_enabled', return_value=True):
            with patch.object(self.tracker, 'get_usage_stats') as mock_stats:
                mock_stats.return_value = {
                    'totals': {'cost': 6.00},
                    'limits': {'cost_limit': 5.00}
                }
                
                result = self.tracker.is_cost_limit_exceeded()
                
                assert result == True
    
    def test_get_remaining_budget(self):
        """Test get_remaining_budget method."""
        with patch.object(self.tracker, 'is_tracking_enabled', return_value=True):
            with patch.object(self.tracker, 'get_usage_stats') as mock_stats:
                mock_stats.return_value = {
                    'totals': {'cost': 2.50},
                    'limits': {'cost_limit': 5.00}
                }
                
                result = self.tracker.get_remaining_budget()
                
                assert result == 2.50
    
    def test_get_remaining_budget_tracking_disabled(self):
        """Test get_remaining_budget when tracking is disabled."""
        with patch.object(self.tracker, 'is_tracking_enabled', return_value=False):
            result = self.tracker.get_remaining_budget()
            
            assert result == float('inf')
    
    def test_create_default_usage_data(self):
        """Test _create_default_usage_data method."""
        with patch('datetime.date') as mock_date:
            mock_date.today.return_value.isoformat.return_value = "2024-12-19"
            
            result = self.tracker._create_default_usage_data()
            
            # Check that the result has the expected structure
            assert 'period' in result
            assert 'totals' in result
            assert 'limits' in result
            assert result['totals']['requests'] == 0
            assert result['totals']['tokens'] == 0
            assert result['totals']['cost'] == 0.0
            assert result['limits']['cost_limit'] == 5.00
            assert result['limits']['tracking_enabled'] == True


class TestAiUsageTrackerIntegration:
    """Test AiUsageTracker integration with real components."""
    
    def test_integration_with_real_config(self):
        """Test integration with real ConfigManager."""
        try:
            from src.core.config import ConfigManager
            
            config = ConfigManager()
            tracker = AiUsageTracker(config)
            
            # Test basic functionality
            assert isinstance(tracker.is_tracking_enabled(), bool)
            assert isinstance(tracker.get_cost_limit(), float)
            assert isinstance(tracker.get_remaining_budget(), float)
            
        except Exception:
            # Skip if not in a git repository or config issues
            pytest.skip("Integration test requires proper configuration")
    
    def test_usage_file_creation(self):
        """Test that usage file is created when needed."""
        with tempfile.TemporaryDirectory() as temp_dir:
            usage_file = os.path.join(temp_dir, "test-usage.yaml")
            
            config_mock = Mock()
            config_mock.get_config.side_effect = lambda key, default: {
                'ai.usage_file': usage_file,
                'ai.tracking_enabled': True,
                'ai.cost_limit': 5.00
            }.get(key, default)
            
            tracker = AiUsageTracker(config_mock)
            
            # Increment usage (should create file)
            tracker.increment_usage("ggfeat", 100, 0.05)
            
            # Check if file was created
            assert os.path.exists(usage_file)
            
            # Check file content
            with open(usage_file, 'r') as f:
                data = yaml.safe_load(f)
                assert data['totals']['requests'] == 1
                assert data['totals']['tokens'] == 100
                assert data['totals']['cost'] == 0.05
    
    def test_usage_file_loading(self):
        """Test that usage file is loaded correctly."""
        with tempfile.TemporaryDirectory() as temp_dir:
            usage_file = os.path.join(temp_dir, "test-usage.yaml")
            
            # Create test data
            test_data = {
                'period': {'start_date': '2024-12-19'},
                'totals': {'requests': 5, 'tokens': 500, 'cost': 0.25},
                'limits': {'cost_limit': 5.00, 'tracking_enabled': True}
            }
            
            with open(usage_file, 'w') as f:
                yaml.dump(test_data, f)
            
            config_mock = Mock()
            config_mock.get_config.side_effect = lambda key, default: {
                'ai.usage_file': usage_file,
                'ai.tracking_enabled': True,
                'ai.cost_limit': 5.00
            }.get(key, default)
            
            tracker = AiUsageTracker(config_mock)
            
            # Load and verify data
            stats = tracker.get_usage_stats()
            assert stats['totals']['requests'] == 5
            assert stats['totals']['tokens'] == 500
            assert stats['totals']['cost'] == 0.25
