/**
 * Soul Forge Canon — International Gendered-(all) STEM Professional Unified Canon
 * 
 * @module @babel-canon/soul-forge
 * @version 1.0.0
 * @license Soul-Forge-1.0
 */

const fs = require('fs');
const path = require('path');

const CANON_METADATA = {
  name: '@babel-canon/soul-forge',
  version: '1.0.0',
  name: 'Soul Forge Canon',
  description: 'International Gendered-(all) STEM Professional Unified Canon',
  license: 'Soul-Forge-1.0',
  licenseUrl: 'https://github.com/myzticalbabe/babel/blob/master/LICENSE',
  repository: 'https://github.com/myzticalbabe/babel',
  books: [
    { id: 1, title: 'Soul Forge License v1.0', file: 'LICENSE', vow: 'Governance' },
    { id: 2, title: 'Accessibility Mandate', file: 'ACCESSIBILITY.md', vow: 'Vow II' },
    { id: 3, title: 'Gender-Inclusive STEM Standards', file: 'STEM.md', vow: 'Six Practices' },
    { id: 4, title: 'Professional Conduct', file: 'CONDUCT.md', vow: 'Vows Applied' },
    { id: 5, title: 'Mentorship & Role Model Registry', file: 'ROLE_MODELS.md', vow: 'Springer 2026' },
    { id: 6, title: 'Assessment & Certification', file: 'ASSESSMENT.md', vow: 'Mastery + Identity' },
    { id: 7, title: 'Audit & Compliance', file: 'AUDIT.md', vow: 'Two Auditors' },
    { id: 8, title: 'DEI Mandates', file: 'DEI_MANDATES.md', vow: 'Eight Edicts' }
  ],
  skills: [
    'FACILITATION_SKILLS',
    'ASSESSMENT_TECHNIQUES', 
    'ICEBREAKER_LIBRARY',
    'FAMILY_ENGAGEMENT_PACK',
    'STRUGGLE_JOURNAL'
  ],
  tools: [
    'audit_inclusion.py',
    'audit_accessibility.py',
    'generate_lesson.py'
  ],
  governance: {
    council: [
      { role: 'Forge Keeper', status: 'filled', term: 'indefinite' },
      { role: 'Accessibility Guardian', status: 'vacant', term: '2 years' },
      { role: 'Equity Steward', status: 'vacant', term: '2 years' },
      { role: 'Canon Scribe', status: 'vacant', term: '2 years' }
    ],
    decisionRule: '2/3 consensus, veto only on Soul Forge License violations'
  },
  mandates: {
    dei: 'DEI_MANDATES.md',
    implementation: '2026-12-31 through 2027-12-31'
  }
};

function getCanonMetadata() {
  return CANON_METADATA;
}

function getBook(bookId) {
  const bookFiles = {
    1: 'LICENSE',
    2: 'ACCESSIBILITY.md',
    3: 'STEM.md',
    4: 'CONDUCT.md',
    5: 'ROLE_MODELS.md',
    6: 'ASSESSMENT.md',
    7: 'AUDIT.md',
    8: 'DEI_MANDATES.md'
  };
  
  const file = bookFiles[bookId];
  if (!file) return null;
  
  const filePath = path.join(__dirname, file);
  if (!fs.existsSync(filePath)) return null;
  
  return fs.readFileSync(filePath, 'utf-8');
}

function getSkill(skillName) {
  const filePath = path.join(__dirname, 'skills', `${skillName}.md`);
  if (!fs.existsSync(filePath)) return null;
  return fs.readFileSync(filePath, 'utf-8');
}

function getRoleModel(roleModelId) {
  const filePath = path.join(__dirname, 'ROLE_MODELS', `${roleModelId}.json`);
  if (!fs.existsSync(filePath)) return null;
  return JSON.parse(fs.readFileSync(filePath, 'utf-8'));
}

function listRoleModels() {
  const dir = path.join(__dirname, 'ROLE_MODELS');
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter(f => f.endsWith('.json')).map(f => f.replace('.json', ''));
}

function runInclusionAudit(options = {}) {
  const { spawnSync } = require('child_process');
  const result = spawnSync('python', [
    path.join(__dirname, 'tools', 'audit_inclusion.py'),
    '--path', options.path || '.',
    '--fail-on', options.failOn || 'high',
    ...(options.json ? ['--json', options.json] : [])
  ], { encoding: 'utf-8', cwd: __dirname });
  return {
    success: result.status === 0,
    stdout: result.stdout,
    stderr: result.stderr
  };
}

function runAccessibilityAudit(options = {}) {
  const { spawnSync } = require('child_process');
  const result = spawnSync('python', [
    path.join(__dirname, 'tools', 'audit_accessibility.py'),
    '--path', options.path || '.',
    '--fail-on', options.failOn || 'critical',
    ...(options.json ? ['--json', options.json] : [])
  ], { encoding: 'utf-8', cwd: __dirname });
  return {
    success: result.status === 0,
    stdout: result.stdout,
    stderr: result.stderr
  };
}

function generateLesson(options = {}) {
  const { spawnSync } = require('child_process');
  const args = [
    path.join(__dirname, 'tools', 'generate_lesson.py'),
    '--topic', options.topic,
    '--grade', options.grade,
    ...(options.standard ? ['--standard', options.standard] : []),
    ...(options.duration ? ['--duration', options.duration] : []),
    ...(options.outputDir ? ['--output-dir', options.outputDir] : [])
  ];
  const result = spawnSync('python', args, { encoding: 'utf-8', cwd: __dirname });
  return {
    success: result.status === 0,
    stdout: result.stdout,
    stderr: result.stderr
  };
}

module.exports = {
  metadata: CANON_METADATA,
  getCanonMetadata,
  getBook,
  getSkill,
  getRoleModel,
  listRoleModels,
  runInclusionAudit,
  runAccessibilityAudit,
  generateLesson
};