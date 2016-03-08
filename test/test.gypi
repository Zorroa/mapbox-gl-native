{
  'includes': [
    '../gyp/common.gypi',
  ],
  'targets': [
    { 'target_name': 'symlink_TEST_DATA',
      'type': 'none',
      'hard_dependency': 1,
      'actions': [
        {
          'action_name': 'Symlink Fixture Directory',
          'inputs': ['<!@(pwd)/../test'],
          'outputs': ['<(PRODUCT_DIR)/TEST_DATA'], # symlinks the test dir into TEST_DATA
          'action': ['ln', '-s', '-f', '-n', '<@(_inputs)', '<@(_outputs)' ],
        }
      ],
    },
    { 'target_name': 'test',
      'type': 'executable',
      'include_dirs': [ '../include', '../src', '../platform/default' ],
      'dependencies': [
        'symlink_TEST_DATA',
        'mbgl.gyp:core',
        'mbgl.gyp:platform-<(platform_lib)',
        'mbgl.gyp:http-<(http_lib)',
        'mbgl.gyp:asset-<(asset_lib)',
        'mbgl.gyp:headless-<(headless_lib)',
      ],
      'sources': [
        'fixtures/main.cpp',
        'fixtures/stub_file_source.cpp',
        'fixtures/stub_file_source.hpp',
        'fixtures/mock_view.hpp',
        'fixtures/util.hpp',
        'fixtures/util.cpp',
        'fixtures/fixture_log_observer.hpp',
        'fixtures/fixture_log_observer.cpp',

        'algorithm/covered_by_children.cpp',
        'algorithm/generate_clip_ids.cpp',

        'util/assert.cpp',
        'util/async_task.cpp',
        'util/geo.cpp',
        'util/image.cpp',
        'util/mapbox.cpp',
        'util/merge_lines.cpp',
        'util/run_loop.cpp',
        'util/text_conversions.cpp',
        'util/thread.cpp',
        'util/thread_local.cpp',
        'util/tile_cover.cpp',
        'util/timer.cpp',
        'util/token.cpp',
        'util/work_queue.cpp',

        'api/annotations.cpp',
        'api/api_misuse.cpp',
        'api/repeated_render.cpp',
        'api/render_missing.cpp',
        'api/set_style.cpp',
        'api/custom_layer.cpp',
        'api/offline.cpp',

        'geometry/binpack.cpp',

        'map/map.cpp',
        'map/map_context.cpp',
        'map/tile.cpp',
        'map/transform.cpp',

        'tile/tile_id.cpp',

        'storage/storage.hpp',
        'storage/storage.cpp',
        'storage/default_file_source.cpp',
        'storage/offline.cpp',
        'storage/offline_database.cpp',
        'storage/offline_download.cpp',
        'storage/asset_file_source.cpp',
        'storage/headers.cpp',
        'storage/http_cancel.cpp',
        'storage/http_error.cpp',
        'storage/http_expires.cpp',
        'storage/http_header_parsing.cpp',
        'storage/http_issue_1369.cpp',
        'storage/http_load.cpp',
        'storage/http_other_loop.cpp',
        'storage/http_retry_network_status.cpp',
        'storage/http_reading.cpp',
        'storage/http_timeout.cpp',
        'storage/resource.cpp',

        'style/glyph_store.cpp',
        'style/source.cpp',
        'style/style.cpp',
        'style/style_layer.cpp',
        'style/comparisons.cpp',
        'style/functions.cpp',
        'style/style_parser.cpp',
        'style/variant.cpp',

        'sprite/sprite_atlas.cpp',
        'sprite/sprite_image.cpp',
        'sprite/sprite_parser.cpp',
        'sprite/sprite_store.cpp',
      ],
      'variables': {
        'cflags_cc': [
          '<@(gtest_cflags)',
          '<@(opengl_cflags)',
          '<@(boost_cflags)',
          '<@(sqlite_cflags)',
          '<@(geojsonvt_cflags)',
          '<@(rapidjson_cflags)',
          '<@(pixelmatch_cflags)',
          '<@(variant_cflags)',
        ],
        'ldflags': [
          '<@(gtest_ldflags)',
          '<@(sqlite_ldflags)',
        ],
        'libraries': [
          '<@(gtest_static_libs)',
          '<@(sqlite_static_libs)',
          '<@(geojsonvt_static_libs)',
        ],
      },
      'conditions': [
        ['OS == "mac"', {
          'xcode_settings': {
            'OTHER_CPLUSPLUSFLAGS': [ '<@(cflags_cc)' ],
          },
        }, {
         'cflags_cc': [ '<@(cflags_cc)' ],
        }],
      ],
      'link_settings': {
        'conditions': [
          ['OS == "mac"', {
            'libraries': [ '<@(libraries)' ],
            'xcode_settings': { 'OTHER_LDFLAGS': [ '<@(ldflags)' ] }
          }, {
            'libraries': [ '<@(libraries)', '<@(ldflags)' ],
          }]
        ],
      },
    },
  ]
}
