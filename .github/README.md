# GitHub Configuration for ggGit

This directory contains all GitHub-specific configurations for the ggGit project.

## 📁 Directory Structure

```
.github/
├── ISSUE_TEMPLATE/          # Issue templates for bug reports, features, and help
├── linters/                 # Linting configuration files
├── workflows/               # GitHub Actions workflows
├── CODEOWNERS              # Code ownership definitions
├── dependabot.yml          # Dependency update automation
├── FUNDING.yml             # Sponsorship configuration
├── pull_request_template.md # PR template
└── README.md               # This file
```

## 🚀 GitHub Actions Workflows

### Core Testing Workflows

1. **`ci.yml`** - Main Continuous Integration pipeline
   - Quick validation
   - Command testing
   - Cross-platform testing
   - Security & quality checks
   - Integration testing
   - Final validation

2. **`test-commands.yml`** - Comprehensive command testing
   - Health check execution
   - Individual command testing
   - Syntax validation
   - Error handling tests
   - Utility function tests

3. **`cross-platform-test.yml`** - Multi-platform compatibility
   - Ubuntu Linux testing
   - macOS testing
   - Windows (Git Bash) testing
   - Windows (PowerShell) testing

4. **`integration-test.yml`** - Real-world usage simulation
   - Git repository setup
   - Basic workflow testing
   - Conventional commits testing
   - Error handling validation
   - Cross-command compatibility

5. **`security-lint.yml`** - Security and code quality
   - ShellCheck linting
   - Security pattern detection
   - Code quality validation
   - File permission checks

6. **`performance-test.yml`** - Performance benchmarking
   - Execution time testing
   - Memory usage analysis
   - Repository size impact
   - Concurrent execution testing

7. **`release.yml`** - Automated releases
   - Tag-based releases
   - Release notes generation
   - Health check validation

### Workflow Triggers

- **Push to main/master**: Full test suite
- **Pull Requests**: Full test suite
- **Tags (v*)** : Release workflow
- **Manual dispatch**: All workflows available

## 🐛 Issue Templates

### Bug Report Template
- Comprehensive bug description
- Reproduction steps
- Expected vs actual behavior
- System information
- ggconfig output requirement

### Feature Request Template
- Feature description and use case
- Proposed solution
- Priority and impact assessment
- Examples and mockups

### Help Wanted Template
- Clear problem description
- Steps already tried
- System configuration
- Expected behavior

## 🔧 Configuration Files

### ShellCheck Configuration (`.shellcheckrc`)
- Disables specific warnings for our use case
- Enables all other checks
- Sets severity level to style

### Dependabot Configuration
- Weekly updates for GitHub Actions
- Weekly updates for npm packages (future)
- Automatic PR creation with labels

### Code Owners
- @novafuria responsible for entire project
- Specific ownership for different areas

## 📋 Pull Request Template

Comprehensive PR template with:
- Change type classification
- Testing checklist
- Breaking changes documentation
- Impact assessment

## 🚀 Getting Started

### For Contributors
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run local tests: `./health-check.sh`
5. Submit a PR using the template

### For Maintainers
1. Review PRs using the checklist
2. Ensure all workflows pass
3. Merge when ready
4. Create releases by pushing tags

## 🔍 Monitoring

- **Workflow Status**: Check Actions tab for current status
- **Test Results**: All workflows provide detailed output
- **Performance Metrics**: Performance workflow tracks execution times
- **Security Alerts**: Security workflow detects potential issues

## 🛠️ Customization

### Adding New Workflows
1. Create `.yml` file in `workflows/` directory
2. Define triggers and jobs
3. Test locally if possible
4. Commit and push

### Modifying Templates
1. Edit files in `ISSUE_TEMPLATE/` directory
2. Test with new issues/PRs
3. Update documentation if needed

### Adding New Linters
1. Create configuration in `linters/` directory
2. Update workflow files to use new linter
3. Test with sample code

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [ShellCheck Documentation](https://www.shellcheck.net/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [ggGit Contributing Guide](../CONTRIBUTING.md)

## 🤝 Support

For questions about GitHub configuration:
- Check existing workflows and templates
- Review the main [CONTRIBUTING.md](../CONTRIBUTING.md)
- Open an issue using the appropriate template
- Contact @novafuria for complex configuration questions
