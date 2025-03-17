# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

GDCMCONV_FS_METADATA = Metadata(
    id="98f7b1994832a771c3433368967176f42a435bc4.boutiques",
    name="gdcmconv.fs",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


GdcmconvFsParameters = typing.TypedDict('GdcmconvFsParameters', {
    "__STYX_TYPE__": typing.Literal["gdcmconv.fs"],
    "input_file": InputPathType,
    "output_file": str,
    "explicit_flag": bool,
    "implicit_flag": bool,
    "use_dict_flag": bool,
    "with_private_dict_flag": bool,
    "check_meta_flag": bool,
    "root_uid": typing.NotRequired[str | None],
    "remove_gl_flag": bool,
    "remove_private_tags_flag": bool,
    "remove_retired_flag": bool,
    "apply_lut_flag": bool,
    "photometric_interpretation": typing.NotRequired[str | None],
    "raw_flag": bool,
    "deflated_flag": bool,
    "jpeg_flag": bool,
    "j2k_flag": bool,
    "jpegls_flag": bool,
    "rle_flag": bool,
    "force_flag": bool,
    "generate_icon_flag": bool,
    "icon_minmax": typing.NotRequired[list[float] | None],
    "icon_auto_minmax_flag": bool,
    "compress_icon_flag": bool,
    "planar_configuration": typing.NotRequired[str | None],
    "lossy_flag": bool,
    "split": typing.NotRequired[float | None],
    "verbose_flag": bool,
    "warning_flag": bool,
    "debug_flag": bool,
    "error_flag": bool,
    "quiet_flag": bool,
    "jpeg_quality": typing.NotRequired[float | None],
    "lossy_error": typing.NotRequired[int | None],
    "rate": typing.NotRequired[float | None],
    "j2k_quality": typing.NotRequired[float | None],
    "tile": typing.NotRequired[list[float] | None],
    "number_resolution": typing.NotRequired[float | None],
    "irreversible_flag": bool,
    "ignore_errors_flag": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "gdcmconv.fs": gdcmconv_fs_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


class GdcmconvFsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gdcmconv_fs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def gdcmconv_fs_params(
    input_file: InputPathType,
    output_file: str,
    explicit_flag: bool = False,
    implicit_flag: bool = False,
    use_dict_flag: bool = False,
    with_private_dict_flag: bool = False,
    check_meta_flag: bool = False,
    root_uid: str | None = None,
    remove_gl_flag: bool = False,
    remove_private_tags_flag: bool = False,
    remove_retired_flag: bool = False,
    apply_lut_flag: bool = False,
    photometric_interpretation: str | None = None,
    raw_flag: bool = False,
    deflated_flag: bool = False,
    jpeg_flag: bool = False,
    j2k_flag: bool = False,
    jpegls_flag: bool = False,
    rle_flag: bool = False,
    force_flag: bool = False,
    generate_icon_flag: bool = False,
    icon_minmax: list[float] | None = None,
    icon_auto_minmax_flag: bool = False,
    compress_icon_flag: bool = False,
    planar_configuration: str | None = None,
    lossy_flag: bool = False,
    split: float | None = None,
    verbose_flag: bool = False,
    warning_flag: bool = False,
    debug_flag: bool = False,
    error_flag: bool = False,
    quiet_flag: bool = False,
    jpeg_quality: float | None = None,
    lossy_error: int | None = None,
    rate: float | None = None,
    j2k_quality: float | None = None,
    tile: list[float] | None = None,
    number_resolution: float | None = None,
    irreversible_flag: bool = False,
    ignore_errors_flag: bool = False,
) -> GdcmconvFsParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input DICOM filename.
        output_file: Output DICOM filename.
        explicit_flag: Change Transfer Syntax to explicit.
        implicit_flag: Change Transfer Syntax to implicit.
        use_dict_flag: Use dict for VR (only public by default).
        with_private_dict_flag: Use private dict for VR (advanced user only).
        check_meta_flag: Check File Meta Information (advanced user only).
        root_uid: Root UID.
        remove_gl_flag: Remove group length (deprecated in DICOM 2008).
        remove_private_tags_flag: Remove private tags.
        remove_retired_flag: Remove retired tags.
        apply_lut_flag: Apply LUT (non-standard, advanced user only).
        photometric_interpretation: Change Photometric Interpretation (when\
            possible).
        raw_flag: Decompress image.
        deflated_flag: Compress using deflated (gzip).
        jpeg_flag: Compress image in jpeg.
        j2k_flag: Compress image in j2k.
        jpegls_flag: Compress image in jpeg-ls.
        rle_flag: Compress image in rle (lossless only).
        force_flag: Force decompression/merging before recompression/splitting.
        generate_icon_flag: Generate icon.
        icon_minmax: Min/Max value for icon.
        icon_auto_minmax_flag: Automatically compute best Min/Max values for\
            icon.
        compress_icon_flag: Decide whether icon follows main Transfer Syntax or\
            remains uncompressed.
        planar_configuration: Change planar configuration.
        lossy_flag: Use the lossy (if possible) compressor.
        split: Write 2D image with multiple fragments (using max size).
        verbose_flag: More verbose (warning+error).
        warning_flag: Print warning info.
        debug_flag: Print debug info.
        error_flag: Print error info.
        quiet_flag: Do not print to stdout.
        jpeg_quality: Set JPEG quality.
        lossy_error: Set JPEG-LS lossy error.
        rate: Set J2K rate.
        j2k_quality: Set J2K quality.
        tile: Set J2K tile size.
        number_resolution: Set number of resolution.
        irreversible_flag: Set irreversible.
        ignore_errors_flag: Convert even if file is corrupted (advanced users\
            only, see disclaimers).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "gdcmconv.fs",
        "input_file": input_file,
        "output_file": output_file,
        "explicit_flag": explicit_flag,
        "implicit_flag": implicit_flag,
        "use_dict_flag": use_dict_flag,
        "with_private_dict_flag": with_private_dict_flag,
        "check_meta_flag": check_meta_flag,
        "remove_gl_flag": remove_gl_flag,
        "remove_private_tags_flag": remove_private_tags_flag,
        "remove_retired_flag": remove_retired_flag,
        "apply_lut_flag": apply_lut_flag,
        "raw_flag": raw_flag,
        "deflated_flag": deflated_flag,
        "jpeg_flag": jpeg_flag,
        "j2k_flag": j2k_flag,
        "jpegls_flag": jpegls_flag,
        "rle_flag": rle_flag,
        "force_flag": force_flag,
        "generate_icon_flag": generate_icon_flag,
        "icon_auto_minmax_flag": icon_auto_minmax_flag,
        "compress_icon_flag": compress_icon_flag,
        "lossy_flag": lossy_flag,
        "verbose_flag": verbose_flag,
        "warning_flag": warning_flag,
        "debug_flag": debug_flag,
        "error_flag": error_flag,
        "quiet_flag": quiet_flag,
        "irreversible_flag": irreversible_flag,
        "ignore_errors_flag": ignore_errors_flag,
    }
    if root_uid is not None:
        params["root_uid"] = root_uid
    if photometric_interpretation is not None:
        params["photometric_interpretation"] = photometric_interpretation
    if icon_minmax is not None:
        params["icon_minmax"] = icon_minmax
    if planar_configuration is not None:
        params["planar_configuration"] = planar_configuration
    if split is not None:
        params["split"] = split
    if jpeg_quality is not None:
        params["jpeg_quality"] = jpeg_quality
    if lossy_error is not None:
        params["lossy_error"] = lossy_error
    if rate is not None:
        params["rate"] = rate
    if j2k_quality is not None:
        params["j2k_quality"] = j2k_quality
    if tile is not None:
        params["tile"] = tile
    if number_resolution is not None:
        params["number_resolution"] = number_resolution
    return params


def gdcmconv_fs_cargs(
    params: GdcmconvFsParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("gdcmconv.fs")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("output_file"))
    if params.get("explicit_flag"):
        cargs.append("-X")
    if params.get("implicit_flag"):
        cargs.append("-M")
    if params.get("use_dict_flag"):
        cargs.append("-U")
    if params.get("with_private_dict_flag"):
        cargs.append("--with-private-dict")
    if params.get("check_meta_flag"):
        cargs.append("-C")
    if params.get("root_uid") is not None:
        cargs.extend([
            "--root-uid",
            params.get("root_uid")
        ])
    if params.get("remove_gl_flag"):
        cargs.append("--remove-gl")
    if params.get("remove_private_tags_flag"):
        cargs.append("--remove-private-tags")
    if params.get("remove_retired_flag"):
        cargs.append("--remove-retired")
    if params.get("apply_lut_flag"):
        cargs.append("-l")
    if params.get("photometric_interpretation") is not None:
        cargs.extend([
            "-P",
            params.get("photometric_interpretation")
        ])
    if params.get("raw_flag"):
        cargs.append("-w")
    if params.get("deflated_flag"):
        cargs.append("-d")
    if params.get("jpeg_flag"):
        cargs.append("-J")
    if params.get("j2k_flag"):
        cargs.append("-K")
    if params.get("jpegls_flag"):
        cargs.append("-L")
    if params.get("rle_flag"):
        cargs.append("-R")
    if params.get("force_flag"):
        cargs.append("-F")
    if params.get("generate_icon_flag"):
        cargs.append("--generate-icon")
    if params.get("icon_minmax") is not None:
        cargs.extend([
            "--icon-minmax",
            *map(str, params.get("icon_minmax"))
        ])
    if params.get("icon_auto_minmax_flag"):
        cargs.append("--icon-auto-minmax")
    if params.get("compress_icon_flag"):
        cargs.append("--compress-icon")
    if params.get("planar_configuration") is not None:
        cargs.extend([
            "--planar-configuration",
            params.get("planar_configuration")
        ])
    if params.get("lossy_flag"):
        cargs.append("-Y")
    if params.get("split") is not None:
        cargs.extend([
            "-S",
            str(params.get("split"))
        ])
    if params.get("verbose_flag"):
        cargs.append("-V")
    if params.get("warning_flag"):
        cargs.append("-W")
    if params.get("debug_flag"):
        cargs.append("-D")
    if params.get("error_flag"):
        cargs.append("-E")
    if params.get("quiet_flag"):
        cargs.append("--quiet")
    if params.get("jpeg_quality") is not None:
        cargs.extend([
            "-q",
            str(params.get("jpeg_quality"))
        ])
    if params.get("lossy_error") is not None:
        cargs.extend([
            "-e",
            str(params.get("lossy_error"))
        ])
    if params.get("rate") is not None:
        cargs.extend([
            "-r",
            str(params.get("rate"))
        ])
    if params.get("j2k_quality") is not None:
        cargs.extend([
            "-q",
            str(params.get("j2k_quality"))
        ])
    if params.get("tile") is not None:
        cargs.extend([
            "-t",
            *map(str, params.get("tile"))
        ])
    if params.get("number_resolution") is not None:
        cargs.extend([
            "-n",
            str(params.get("number_resolution"))
        ])
    if params.get("irreversible_flag"):
        cargs.append("--irreversible")
    if params.get("ignore_errors_flag"):
        cargs.append("-I")
    return cargs


def gdcmconv_fs_outputs(
    params: GdcmconvFsParameters,
    execution: Execution,
) -> GdcmconvFsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GdcmconvFsOutputs(
        root=execution.output_file("."),
    )
    return ret


def gdcmconv_fs_execute(
    params: GdcmconvFsParameters,
    execution: Execution,
) -> GdcmconvFsOutputs:
    """
    Convert a DICOM file into another DICOM file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GdcmconvFsOutputs`).
    """
    params = execution.params(params)
    cargs = gdcmconv_fs_cargs(params, execution)
    ret = gdcmconv_fs_outputs(params, execution)
    execution.run(cargs)
    return ret


def gdcmconv_fs(
    input_file: InputPathType,
    output_file: str,
    explicit_flag: bool = False,
    implicit_flag: bool = False,
    use_dict_flag: bool = False,
    with_private_dict_flag: bool = False,
    check_meta_flag: bool = False,
    root_uid: str | None = None,
    remove_gl_flag: bool = False,
    remove_private_tags_flag: bool = False,
    remove_retired_flag: bool = False,
    apply_lut_flag: bool = False,
    photometric_interpretation: str | None = None,
    raw_flag: bool = False,
    deflated_flag: bool = False,
    jpeg_flag: bool = False,
    j2k_flag: bool = False,
    jpegls_flag: bool = False,
    rle_flag: bool = False,
    force_flag: bool = False,
    generate_icon_flag: bool = False,
    icon_minmax: list[float] | None = None,
    icon_auto_minmax_flag: bool = False,
    compress_icon_flag: bool = False,
    planar_configuration: str | None = None,
    lossy_flag: bool = False,
    split: float | None = None,
    verbose_flag: bool = False,
    warning_flag: bool = False,
    debug_flag: bool = False,
    error_flag: bool = False,
    quiet_flag: bool = False,
    jpeg_quality: float | None = None,
    lossy_error: int | None = None,
    rate: float | None = None,
    j2k_quality: float | None = None,
    tile: list[float] | None = None,
    number_resolution: float | None = None,
    irreversible_flag: bool = False,
    ignore_errors_flag: bool = False,
    runner: Runner | None = None,
) -> GdcmconvFsOutputs:
    """
    Convert a DICOM file into another DICOM file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input DICOM filename.
        output_file: Output DICOM filename.
        explicit_flag: Change Transfer Syntax to explicit.
        implicit_flag: Change Transfer Syntax to implicit.
        use_dict_flag: Use dict for VR (only public by default).
        with_private_dict_flag: Use private dict for VR (advanced user only).
        check_meta_flag: Check File Meta Information (advanced user only).
        root_uid: Root UID.
        remove_gl_flag: Remove group length (deprecated in DICOM 2008).
        remove_private_tags_flag: Remove private tags.
        remove_retired_flag: Remove retired tags.
        apply_lut_flag: Apply LUT (non-standard, advanced user only).
        photometric_interpretation: Change Photometric Interpretation (when\
            possible).
        raw_flag: Decompress image.
        deflated_flag: Compress using deflated (gzip).
        jpeg_flag: Compress image in jpeg.
        j2k_flag: Compress image in j2k.
        jpegls_flag: Compress image in jpeg-ls.
        rle_flag: Compress image in rle (lossless only).
        force_flag: Force decompression/merging before recompression/splitting.
        generate_icon_flag: Generate icon.
        icon_minmax: Min/Max value for icon.
        icon_auto_minmax_flag: Automatically compute best Min/Max values for\
            icon.
        compress_icon_flag: Decide whether icon follows main Transfer Syntax or\
            remains uncompressed.
        planar_configuration: Change planar configuration.
        lossy_flag: Use the lossy (if possible) compressor.
        split: Write 2D image with multiple fragments (using max size).
        verbose_flag: More verbose (warning+error).
        warning_flag: Print warning info.
        debug_flag: Print debug info.
        error_flag: Print error info.
        quiet_flag: Do not print to stdout.
        jpeg_quality: Set JPEG quality.
        lossy_error: Set JPEG-LS lossy error.
        rate: Set J2K rate.
        j2k_quality: Set J2K quality.
        tile: Set J2K tile size.
        number_resolution: Set number of resolution.
        irreversible_flag: Set irreversible.
        ignore_errors_flag: Convert even if file is corrupted (advanced users\
            only, see disclaimers).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GdcmconvFsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GDCMCONV_FS_METADATA)
    params = gdcmconv_fs_params(
        input_file=input_file,
        output_file=output_file,
        explicit_flag=explicit_flag,
        implicit_flag=implicit_flag,
        use_dict_flag=use_dict_flag,
        with_private_dict_flag=with_private_dict_flag,
        check_meta_flag=check_meta_flag,
        root_uid=root_uid,
        remove_gl_flag=remove_gl_flag,
        remove_private_tags_flag=remove_private_tags_flag,
        remove_retired_flag=remove_retired_flag,
        apply_lut_flag=apply_lut_flag,
        photometric_interpretation=photometric_interpretation,
        raw_flag=raw_flag,
        deflated_flag=deflated_flag,
        jpeg_flag=jpeg_flag,
        j2k_flag=j2k_flag,
        jpegls_flag=jpegls_flag,
        rle_flag=rle_flag,
        force_flag=force_flag,
        generate_icon_flag=generate_icon_flag,
        icon_minmax=icon_minmax,
        icon_auto_minmax_flag=icon_auto_minmax_flag,
        compress_icon_flag=compress_icon_flag,
        planar_configuration=planar_configuration,
        lossy_flag=lossy_flag,
        split=split,
        verbose_flag=verbose_flag,
        warning_flag=warning_flag,
        debug_flag=debug_flag,
        error_flag=error_flag,
        quiet_flag=quiet_flag,
        jpeg_quality=jpeg_quality,
        lossy_error=lossy_error,
        rate=rate,
        j2k_quality=j2k_quality,
        tile=tile,
        number_resolution=number_resolution,
        irreversible_flag=irreversible_flag,
        ignore_errors_flag=ignore_errors_flag,
    )
    return gdcmconv_fs_execute(params, execution)


__all__ = [
    "GDCMCONV_FS_METADATA",
    "GdcmconvFsOutputs",
    "GdcmconvFsParameters",
    "gdcmconv_fs",
    "gdcmconv_fs_params",
]
