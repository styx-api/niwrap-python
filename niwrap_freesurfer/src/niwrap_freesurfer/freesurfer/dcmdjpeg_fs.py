# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DCMDJPEG_FS_METADATA = Metadata(
    id="359bc973b8599706e77b1aca498ebac2ce7ef402.boutiques",
    name="dcmdjpeg.fs",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


DcmdjpegFsParameters = typing.TypedDict('DcmdjpegFsParameters', {
    "__STYXTYPE__": typing.Literal["dcmdjpeg.fs"],
    "input_file": InputPathType,
    "output_file": str,
    "help": bool,
    "version": bool,
    "arguments": bool,
    "quiet": bool,
    "verbose": bool,
    "debug": bool,
    "log_level": typing.NotRequired[str | None],
    "log_config": typing.NotRequired[InputPathType | None],
    "read_file": bool,
    "read_file_only": bool,
    "read_dataset": bool,
    "conv_photometric": bool,
    "conv_lossy": bool,
    "conv_guess": bool,
    "conv_guess_lossy": bool,
    "conv_always": bool,
    "conv_never": bool,
    "planar_auto": bool,
    "color_by_pixel": bool,
    "color_by_plane": bool,
    "uid_default": bool,
    "uid_always": bool,
    "workaround_pred6": bool,
    "workaround_incpl": bool,
    "write_file": bool,
    "write_dataset": bool,
    "write_xfer_little": bool,
    "write_xfer_big": bool,
    "write_xfer_implicit": bool,
    "enable_new_vr": bool,
    "disable_new_vr": bool,
    "group_length_recalc": bool,
    "group_length_create": bool,
    "group_length_remove": bool,
    "length_explicit": bool,
    "length_undefined": bool,
    "padding_retain": bool,
    "padding_off": bool,
    "padding_create": typing.NotRequired[list[float] | None],
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
        "dcmdjpeg.fs": dcmdjpeg_fs_cargs,
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
        "dcmdjpeg.fs": dcmdjpeg_fs_outputs,
    }.get(t)


class DcmdjpegFsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dcmdjpeg_fs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """DICOM output file"""


def dcmdjpeg_fs_params(
    input_file: InputPathType,
    output_file: str,
    help_: bool = False,
    version: bool = False,
    arguments: bool = False,
    quiet: bool = False,
    verbose: bool = False,
    debug: bool = False,
    log_level: str | None = None,
    log_config: InputPathType | None = None,
    read_file: bool = False,
    read_file_only: bool = False,
    read_dataset: bool = False,
    conv_photometric: bool = False,
    conv_lossy: bool = False,
    conv_guess: bool = False,
    conv_guess_lossy: bool = False,
    conv_always: bool = False,
    conv_never: bool = False,
    planar_auto: bool = False,
    color_by_pixel: bool = False,
    color_by_plane: bool = False,
    uid_default: bool = False,
    uid_always: bool = False,
    workaround_pred6: bool = False,
    workaround_incpl: bool = False,
    write_file: bool = False,
    write_dataset: bool = False,
    write_xfer_little: bool = False,
    write_xfer_big: bool = False,
    write_xfer_implicit: bool = False,
    enable_new_vr: bool = False,
    disable_new_vr: bool = False,
    group_length_recalc: bool = False,
    group_length_create: bool = False,
    group_length_remove: bool = False,
    length_explicit: bool = False,
    length_undefined: bool = False,
    padding_retain: bool = False,
    padding_off: bool = False,
    padding_create: list[float] | None = None,
) -> DcmdjpegFsParameters:
    """
    Build parameters.
    
    Args:
        input_file: DICOM input filename to be converted.
        output_file: DICOM output filename.
        help_: Print this help text and exit.
        version: Print version information and exit.
        arguments: Print expanded command line arguments.
        quiet: Quiet mode, print no warnings and errors.
        verbose: Verbose mode, print processing details.
        debug: Debug mode, print debug information.
        log_level: Use level l for the logger (fatal, error, warn, info, debug,\
            trace).
        log_config: Use config file f for the logger.
        read_file: Read file format or data set (default).
        read_file_only: Read file format only.
        read_dataset: Read data set without file meta information.
        conv_photometric: Convert if YCbCr photometric interpretation (default).
        conv_lossy: Convert YCbCr to RGB if lossy JPEG.
        conv_guess: Convert to RGB if YCbCr is guessed by library.
        conv_guess_lossy: Convert to RGB if lossy JPEG and YCbCr is guessed.
        conv_always: Always convert YCbCr to RGB.
        conv_never: Never convert color space.
        planar_auto: Automatically determine planar configuration from SOP\
            class and color space (default).
        color_by_pixel: Always store color-by-pixel.
        color_by_plane: Always store color-by-plane.
        uid_default: Keep same SOP Instance UID (default).
        uid_always: Always assign new UID.
        workaround_pred6: Enable workaround for JPEG lossless images with\
            overflow in predictor 6.
        workaround_incpl: Enable workaround for incomplete JPEG data.
        write_file: Write file format (default).
        write_dataset: Write data set without file meta information.
        write_xfer_little: Write with explicit VR little endian (default).
        write_xfer_big: Write with explicit VR big endian TS.
        write_xfer_implicit: Write with implicit VR little endian TS.
        enable_new_vr: Enable support for new VRs (UN/UT) (default).
        disable_new_vr: Disable support for new VRs, convert to OB.
        group_length_recalc: Recalculate group lengths if present (default).
        group_length_create: Always write with group length elements.
        group_length_remove: Always write without group length elements.
        length_explicit: Write with explicit lengths (default).
        length_undefined: Write with undefined lengths.
        padding_retain: Do not change padding (default if not --write-dataset).
        padding_off: No padding (implicit if --write-dataset).
        padding_create: Align file on multiple of f bytes and items on multiple\
            of i bytes.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dcmdjpeg.fs",
        "input_file": input_file,
        "output_file": output_file,
        "help": help_,
        "version": version,
        "arguments": arguments,
        "quiet": quiet,
        "verbose": verbose,
        "debug": debug,
        "read_file": read_file,
        "read_file_only": read_file_only,
        "read_dataset": read_dataset,
        "conv_photometric": conv_photometric,
        "conv_lossy": conv_lossy,
        "conv_guess": conv_guess,
        "conv_guess_lossy": conv_guess_lossy,
        "conv_always": conv_always,
        "conv_never": conv_never,
        "planar_auto": planar_auto,
        "color_by_pixel": color_by_pixel,
        "color_by_plane": color_by_plane,
        "uid_default": uid_default,
        "uid_always": uid_always,
        "workaround_pred6": workaround_pred6,
        "workaround_incpl": workaround_incpl,
        "write_file": write_file,
        "write_dataset": write_dataset,
        "write_xfer_little": write_xfer_little,
        "write_xfer_big": write_xfer_big,
        "write_xfer_implicit": write_xfer_implicit,
        "enable_new_vr": enable_new_vr,
        "disable_new_vr": disable_new_vr,
        "group_length_recalc": group_length_recalc,
        "group_length_create": group_length_create,
        "group_length_remove": group_length_remove,
        "length_explicit": length_explicit,
        "length_undefined": length_undefined,
        "padding_retain": padding_retain,
        "padding_off": padding_off,
    }
    if log_level is not None:
        params["log_level"] = log_level
    if log_config is not None:
        params["log_config"] = log_config
    if padding_create is not None:
        params["padding_create"] = padding_create
    return params


def dcmdjpeg_fs_cargs(
    params: DcmdjpegFsParameters,
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
    cargs.append("dcmdjpeg.fs")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("output_file"))
    if params.get("help"):
        cargs.append("-h")
    if params.get("version"):
        cargs.append("--version")
    if params.get("arguments"):
        cargs.append("--arguments")
    if params.get("quiet"):
        cargs.append("-q")
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("debug"):
        cargs.append("-d")
    if params.get("log_level") is not None:
        cargs.extend([
            "-ll",
            params.get("log_level")
        ])
    if params.get("log_config") is not None:
        cargs.extend([
            "-lc",
            execution.input_file(params.get("log_config"))
        ])
    if params.get("read_file"):
        cargs.append("+f")
    if params.get("read_file_only"):
        cargs.append("+fo")
    if params.get("read_dataset"):
        cargs.append("-f")
    if params.get("conv_photometric"):
        cargs.append("+cp")
    if params.get("conv_lossy"):
        cargs.append("+cl")
    if params.get("conv_guess"):
        cargs.append("+cg")
    if params.get("conv_guess_lossy"):
        cargs.append("+cgl")
    if params.get("conv_always"):
        cargs.append("+ca")
    if params.get("conv_never"):
        cargs.append("+cn")
    if params.get("planar_auto"):
        cargs.append("+pa")
    if params.get("color_by_pixel"):
        cargs.append("+px")
    if params.get("color_by_plane"):
        cargs.append("+pl")
    if params.get("uid_default"):
        cargs.append("+ud")
    if params.get("uid_always"):
        cargs.append("+ua")
    if params.get("workaround_pred6"):
        cargs.append("+w6")
    if params.get("workaround_incpl"):
        cargs.append("+wi")
    if params.get("write_file"):
        cargs.append("+F")
    if params.get("write_dataset"):
        cargs.append("-F")
    if params.get("write_xfer_little"):
        cargs.append("+te")
    if params.get("write_xfer_big"):
        cargs.append("+tb")
    if params.get("write_xfer_implicit"):
        cargs.append("+ti")
    if params.get("enable_new_vr"):
        cargs.append("+u")
    if params.get("disable_new_vr"):
        cargs.append("-u")
    if params.get("group_length_recalc"):
        cargs.append("+g=")
    if params.get("group_length_create"):
        cargs.append("+g")
    if params.get("group_length_remove"):
        cargs.append("-g")
    if params.get("length_explicit"):
        cargs.append("+e")
    if params.get("length_undefined"):
        cargs.append("-e")
    if params.get("padding_retain"):
        cargs.append("-p=")
    if params.get("padding_off"):
        cargs.append("-p")
    if params.get("padding_create") is not None:
        cargs.extend([
            "+p",
            *map(str, params.get("padding_create"))
        ])
    return cargs


def dcmdjpeg_fs_outputs(
    params: DcmdjpegFsParameters,
    execution: Execution,
) -> DcmdjpegFsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DcmdjpegFsOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_file")),
    )
    return ret


def dcmdjpeg_fs_execute(
    params: DcmdjpegFsParameters,
    execution: Execution,
) -> DcmdjpegFsOutputs:
    """
    A tool to decode JPEG-compressed DICOM files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DcmdjpegFsOutputs`).
    """
    params = execution.params(params)
    cargs = dcmdjpeg_fs_cargs(params, execution)
    ret = dcmdjpeg_fs_outputs(params, execution)
    execution.run(cargs)
    return ret


def dcmdjpeg_fs(
    input_file: InputPathType,
    output_file: str,
    help_: bool = False,
    version: bool = False,
    arguments: bool = False,
    quiet: bool = False,
    verbose: bool = False,
    debug: bool = False,
    log_level: str | None = None,
    log_config: InputPathType | None = None,
    read_file: bool = False,
    read_file_only: bool = False,
    read_dataset: bool = False,
    conv_photometric: bool = False,
    conv_lossy: bool = False,
    conv_guess: bool = False,
    conv_guess_lossy: bool = False,
    conv_always: bool = False,
    conv_never: bool = False,
    planar_auto: bool = False,
    color_by_pixel: bool = False,
    color_by_plane: bool = False,
    uid_default: bool = False,
    uid_always: bool = False,
    workaround_pred6: bool = False,
    workaround_incpl: bool = False,
    write_file: bool = False,
    write_dataset: bool = False,
    write_xfer_little: bool = False,
    write_xfer_big: bool = False,
    write_xfer_implicit: bool = False,
    enable_new_vr: bool = False,
    disable_new_vr: bool = False,
    group_length_recalc: bool = False,
    group_length_create: bool = False,
    group_length_remove: bool = False,
    length_explicit: bool = False,
    length_undefined: bool = False,
    padding_retain: bool = False,
    padding_off: bool = False,
    padding_create: list[float] | None = None,
    runner: Runner | None = None,
) -> DcmdjpegFsOutputs:
    """
    A tool to decode JPEG-compressed DICOM files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: DICOM input filename to be converted.
        output_file: DICOM output filename.
        help_: Print this help text and exit.
        version: Print version information and exit.
        arguments: Print expanded command line arguments.
        quiet: Quiet mode, print no warnings and errors.
        verbose: Verbose mode, print processing details.
        debug: Debug mode, print debug information.
        log_level: Use level l for the logger (fatal, error, warn, info, debug,\
            trace).
        log_config: Use config file f for the logger.
        read_file: Read file format or data set (default).
        read_file_only: Read file format only.
        read_dataset: Read data set without file meta information.
        conv_photometric: Convert if YCbCr photometric interpretation (default).
        conv_lossy: Convert YCbCr to RGB if lossy JPEG.
        conv_guess: Convert to RGB if YCbCr is guessed by library.
        conv_guess_lossy: Convert to RGB if lossy JPEG and YCbCr is guessed.
        conv_always: Always convert YCbCr to RGB.
        conv_never: Never convert color space.
        planar_auto: Automatically determine planar configuration from SOP\
            class and color space (default).
        color_by_pixel: Always store color-by-pixel.
        color_by_plane: Always store color-by-plane.
        uid_default: Keep same SOP Instance UID (default).
        uid_always: Always assign new UID.
        workaround_pred6: Enable workaround for JPEG lossless images with\
            overflow in predictor 6.
        workaround_incpl: Enable workaround for incomplete JPEG data.
        write_file: Write file format (default).
        write_dataset: Write data set without file meta information.
        write_xfer_little: Write with explicit VR little endian (default).
        write_xfer_big: Write with explicit VR big endian TS.
        write_xfer_implicit: Write with implicit VR little endian TS.
        enable_new_vr: Enable support for new VRs (UN/UT) (default).
        disable_new_vr: Disable support for new VRs, convert to OB.
        group_length_recalc: Recalculate group lengths if present (default).
        group_length_create: Always write with group length elements.
        group_length_remove: Always write without group length elements.
        length_explicit: Write with explicit lengths (default).
        length_undefined: Write with undefined lengths.
        padding_retain: Do not change padding (default if not --write-dataset).
        padding_off: No padding (implicit if --write-dataset).
        padding_create: Align file on multiple of f bytes and items on multiple\
            of i bytes.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DcmdjpegFsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DCMDJPEG_FS_METADATA)
    params = dcmdjpeg_fs_params(
        input_file=input_file,
        output_file=output_file,
        help_=help_,
        version=version,
        arguments=arguments,
        quiet=quiet,
        verbose=verbose,
        debug=debug,
        log_level=log_level,
        log_config=log_config,
        read_file=read_file,
        read_file_only=read_file_only,
        read_dataset=read_dataset,
        conv_photometric=conv_photometric,
        conv_lossy=conv_lossy,
        conv_guess=conv_guess,
        conv_guess_lossy=conv_guess_lossy,
        conv_always=conv_always,
        conv_never=conv_never,
        planar_auto=planar_auto,
        color_by_pixel=color_by_pixel,
        color_by_plane=color_by_plane,
        uid_default=uid_default,
        uid_always=uid_always,
        workaround_pred6=workaround_pred6,
        workaround_incpl=workaround_incpl,
        write_file=write_file,
        write_dataset=write_dataset,
        write_xfer_little=write_xfer_little,
        write_xfer_big=write_xfer_big,
        write_xfer_implicit=write_xfer_implicit,
        enable_new_vr=enable_new_vr,
        disable_new_vr=disable_new_vr,
        group_length_recalc=group_length_recalc,
        group_length_create=group_length_create,
        group_length_remove=group_length_remove,
        length_explicit=length_explicit,
        length_undefined=length_undefined,
        padding_retain=padding_retain,
        padding_off=padding_off,
        padding_create=padding_create,
    )
    return dcmdjpeg_fs_execute(params, execution)


__all__ = [
    "DCMDJPEG_FS_METADATA",
    "DcmdjpegFsOutputs",
    "DcmdjpegFsParameters",
    "dcmdjpeg_fs",
    "dcmdjpeg_fs_params",
]
