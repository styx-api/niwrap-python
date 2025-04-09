# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RETRO_TS_PY_METADATA = Metadata(
    id="79fe337b0aef3f964a4c552f4dbbd2809f5b1792.boutiques",
    name="RetroTS.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


RetroTsPyParameters = typing.TypedDict('RetroTsPyParameters', {
    "__STYX_TYPE__": typing.Literal["RetroTS.py"],
    "resp_file": typing.NotRequired[InputPathType | None],
    "card_file": typing.NotRequired[InputPathType | None],
    "phys_fs": typing.NotRequired[float | None],
    "num_slices": float,
    "volume_tr": float,
    "phys_file": typing.NotRequired[InputPathType | None],
    "phys_json": typing.NotRequired[InputPathType | None],
    "prefix": typing.NotRequired[str | None],
    "rvt_shifts": typing.NotRequired[str | None],
    "rvt_out": bool,
    "resp_cutoff_freq": typing.NotRequired[float | None],
    "cardiac_cutoff_freq": typing.NotRequired[float | None],
    "cardiac_out": bool,
    "respiration_out": bool,
    "interp_style": typing.NotRequired[str | None],
    "fir_order": typing.NotRequired[float | None],
    "quiet": bool,
    "demo": bool,
    "show_graphs": bool,
    "debug": bool,
    "slice_offset": typing.NotRequired[str | None],
    "slice_major": typing.NotRequired[float | None],
    "slice_order": typing.NotRequired[str | None],
    "zero_phase_offset": bool,
    "legacy_transform": typing.NotRequired[float | None],
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
        "RetroTS.py": retro_ts_py_cargs,
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
        "RetroTS.py": retro_ts_py_outputs,
    }.get(t)


class RetroTsPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `retro_ts_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Output file containing respiratory and cardiac regressors"""


def retro_ts_py_params(
    num_slices: float,
    volume_tr: float,
    resp_file: InputPathType | None = None,
    card_file: InputPathType | None = None,
    phys_fs: float | None = None,
    phys_file: InputPathType | None = None,
    phys_json: InputPathType | None = None,
    prefix: str | None = None,
    rvt_shifts: str | None = None,
    rvt_out: bool = False,
    resp_cutoff_freq: float | None = None,
    cardiac_cutoff_freq: float | None = None,
    cardiac_out: bool = False,
    respiration_out: bool = False,
    interp_style: str | None = None,
    fir_order: float | None = None,
    quiet: bool = False,
    demo: bool = False,
    show_graphs: bool = False,
    debug: bool = False,
    slice_offset: str | None = None,
    slice_major: float | None = None,
    slice_order: str | None = None,
    zero_phase_offset: bool = False,
    legacy_transform: float | None = None,
) -> RetroTsPyParameters:
    """
    Build parameters.
    
    Args:
        num_slices: Number of slices.
        volume_tr: Volume TR in seconds.
        resp_file: Respiration data file.
        card_file: Cardiac data file.
        phys_fs: Physiological signal sampling frequency in Hz.
        phys_file: BIDS formatted physio file in tab-separated format, can be\
            gzipped.
        phys_json: BIDS formatted physio metadata json file. If not specified,\
            the json corresponding to the phys_file will be loaded.
        prefix: Prefix of output file.
        rvt_shifts: Vector of shifts in seconds of RVT signal. (default is\
            [0:5:20]).
        rvt_out: Flag for writing RVT regressors (default is 1).
        resp_cutoff_freq: Cut-off frequency in Hz for respiratory lowpass\
            filter (default 3 Hz).
        cardiac_cutoff_freq: Cut-off frequency in Hz for cardiac lowpass filter\
            (default 3 Hz).
        cardiac_out: Flag for writing Cardiac regressors (default is 1).
        respiration_out: Flag for writing Respiratory regressors (default is 1).
        interp_style: Resampling kernel (default is 'linear').
        fir_order: Order of FIR filter (default is 40).
        quiet: Show talkative progress as the program runs (default is 1).
        demo: Run demonstration of RetroTS (default is 0).
        show_graphs: Show graphs (default is unset; set with any parameter to\
            view).
        debug: Drop into pdb upon an exception (default is False).
        slice_offset: Vector of slice acquisition time offsets in seconds\
            (default is equivalent of alt+z).
        slice_major: Unknown parameter (default is 1).
        slice_order: Slice timing information in seconds. (default is alt+z).
        zero_phase_offset: Zero phase offset flag.
        legacy_transform: Specify the version of the original Matlab code's\
            transformation (default is 0).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "RetroTS.py",
        "num_slices": num_slices,
        "volume_tr": volume_tr,
        "rvt_out": rvt_out,
        "cardiac_out": cardiac_out,
        "respiration_out": respiration_out,
        "quiet": quiet,
        "demo": demo,
        "show_graphs": show_graphs,
        "debug": debug,
        "zero_phase_offset": zero_phase_offset,
    }
    if resp_file is not None:
        params["resp_file"] = resp_file
    if card_file is not None:
        params["card_file"] = card_file
    if phys_fs is not None:
        params["phys_fs"] = phys_fs
    if phys_file is not None:
        params["phys_file"] = phys_file
    if phys_json is not None:
        params["phys_json"] = phys_json
    if prefix is not None:
        params["prefix"] = prefix
    if rvt_shifts is not None:
        params["rvt_shifts"] = rvt_shifts
    if resp_cutoff_freq is not None:
        params["resp_cutoff_freq"] = resp_cutoff_freq
    if cardiac_cutoff_freq is not None:
        params["cardiac_cutoff_freq"] = cardiac_cutoff_freq
    if interp_style is not None:
        params["interp_style"] = interp_style
    if fir_order is not None:
        params["fir_order"] = fir_order
    if slice_offset is not None:
        params["slice_offset"] = slice_offset
    if slice_major is not None:
        params["slice_major"] = slice_major
    if slice_order is not None:
        params["slice_order"] = slice_order
    if legacy_transform is not None:
        params["legacy_transform"] = legacy_transform
    return params


def retro_ts_py_cargs(
    params: RetroTsPyParameters,
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
    cargs.append("RetroTS.py")
    if params.get("resp_file") is not None:
        cargs.extend([
            "-r",
            execution.input_file(params.get("resp_file"))
        ])
    if params.get("card_file") is not None:
        cargs.extend([
            "-c",
            execution.input_file(params.get("card_file"))
        ])
    if params.get("phys_fs") is not None:
        cargs.extend([
            "-p",
            str(params.get("phys_fs"))
        ])
    cargs.extend([
        "-n",
        str(params.get("num_slices"))
    ])
    cargs.extend([
        "-v",
        str(params.get("volume_tr"))
    ])
    if params.get("phys_file") is not None:
        cargs.extend([
            "-phys_file",
            execution.input_file(params.get("phys_file"))
        ])
    if params.get("phys_json") is not None:
        cargs.extend([
            "-phys_json",
            execution.input_file(params.get("phys_json"))
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("rvt_shifts") is not None:
        cargs.extend([
            "-rvt_shifts",
            params.get("rvt_shifts")
        ])
    if params.get("rvt_out"):
        cargs.append("-rvt_out")
    if params.get("resp_cutoff_freq") is not None:
        cargs.extend([
            "-respiration_cutoff_frequency",
            str(params.get("resp_cutoff_freq"))
        ])
    if params.get("cardiac_cutoff_freq") is not None:
        cargs.extend([
            "-cardiac_cutoff_frequency",
            str(params.get("cardiac_cutoff_freq"))
        ])
    if params.get("cardiac_out"):
        cargs.append("-cardiac_out")
    if params.get("respiration_out"):
        cargs.append("-respiration_out")
    if params.get("interp_style") is not None:
        cargs.extend([
            "-interpolation_style",
            params.get("interp_style")
        ])
    if params.get("fir_order") is not None:
        cargs.extend([
            "-fir_order",
            str(params.get("fir_order"))
        ])
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("demo"):
        cargs.append("-demo")
    if params.get("show_graphs"):
        cargs.append("-show_graphs")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("slice_offset") is not None:
        cargs.extend([
            "-slice_offset",
            params.get("slice_offset")
        ])
    if params.get("slice_major") is not None:
        cargs.extend([
            "-slice_major",
            str(params.get("slice_major"))
        ])
    if params.get("slice_order") is not None:
        cargs.extend([
            "-slice_order",
            params.get("slice_order")
        ])
    if params.get("zero_phase_offset"):
        cargs.append("-zero_phase_offset")
    if params.get("legacy_transform") is not None:
        cargs.extend([
            "-legacy_transform",
            str(params.get("legacy_transform"))
        ])
    return cargs


def retro_ts_py_outputs(
    params: RetroTsPyParameters,
    execution: Execution,
) -> RetroTsPyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RetroTsPyOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("prefix") + ".slibase.1D") if (params.get("prefix") is not None) else None,
    )
    return ret


def retro_ts_py_execute(
    params: RetroTsPyParameters,
    execution: Execution,
) -> RetroTsPyOutputs:
    """
    Creates slice-based regressors for regressing out components of heart rate,
    respiration, and respiration volume per time using independent data files or
    BIDS formatted files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RetroTsPyOutputs`).
    """
    params = execution.params(params)
    cargs = retro_ts_py_cargs(params, execution)
    ret = retro_ts_py_outputs(params, execution)
    execution.run(cargs)
    return ret


def retro_ts_py(
    num_slices: float,
    volume_tr: float,
    resp_file: InputPathType | None = None,
    card_file: InputPathType | None = None,
    phys_fs: float | None = None,
    phys_file: InputPathType | None = None,
    phys_json: InputPathType | None = None,
    prefix: str | None = None,
    rvt_shifts: str | None = None,
    rvt_out: bool = False,
    resp_cutoff_freq: float | None = None,
    cardiac_cutoff_freq: float | None = None,
    cardiac_out: bool = False,
    respiration_out: bool = False,
    interp_style: str | None = None,
    fir_order: float | None = None,
    quiet: bool = False,
    demo: bool = False,
    show_graphs: bool = False,
    debug: bool = False,
    slice_offset: str | None = None,
    slice_major: float | None = None,
    slice_order: str | None = None,
    zero_phase_offset: bool = False,
    legacy_transform: float | None = None,
    runner: Runner | None = None,
) -> RetroTsPyOutputs:
    """
    Creates slice-based regressors for regressing out components of heart rate,
    respiration, and respiration volume per time using independent data files or
    BIDS formatted files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        num_slices: Number of slices.
        volume_tr: Volume TR in seconds.
        resp_file: Respiration data file.
        card_file: Cardiac data file.
        phys_fs: Physiological signal sampling frequency in Hz.
        phys_file: BIDS formatted physio file in tab-separated format, can be\
            gzipped.
        phys_json: BIDS formatted physio metadata json file. If not specified,\
            the json corresponding to the phys_file will be loaded.
        prefix: Prefix of output file.
        rvt_shifts: Vector of shifts in seconds of RVT signal. (default is\
            [0:5:20]).
        rvt_out: Flag for writing RVT regressors (default is 1).
        resp_cutoff_freq: Cut-off frequency in Hz for respiratory lowpass\
            filter (default 3 Hz).
        cardiac_cutoff_freq: Cut-off frequency in Hz for cardiac lowpass filter\
            (default 3 Hz).
        cardiac_out: Flag for writing Cardiac regressors (default is 1).
        respiration_out: Flag for writing Respiratory regressors (default is 1).
        interp_style: Resampling kernel (default is 'linear').
        fir_order: Order of FIR filter (default is 40).
        quiet: Show talkative progress as the program runs (default is 1).
        demo: Run demonstration of RetroTS (default is 0).
        show_graphs: Show graphs (default is unset; set with any parameter to\
            view).
        debug: Drop into pdb upon an exception (default is False).
        slice_offset: Vector of slice acquisition time offsets in seconds\
            (default is equivalent of alt+z).
        slice_major: Unknown parameter (default is 1).
        slice_order: Slice timing information in seconds. (default is alt+z).
        zero_phase_offset: Zero phase offset flag.
        legacy_transform: Specify the version of the original Matlab code's\
            transformation (default is 0).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RetroTsPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RETRO_TS_PY_METADATA)
    params = retro_ts_py_params(
        resp_file=resp_file,
        card_file=card_file,
        phys_fs=phys_fs,
        num_slices=num_slices,
        volume_tr=volume_tr,
        phys_file=phys_file,
        phys_json=phys_json,
        prefix=prefix,
        rvt_shifts=rvt_shifts,
        rvt_out=rvt_out,
        resp_cutoff_freq=resp_cutoff_freq,
        cardiac_cutoff_freq=cardiac_cutoff_freq,
        cardiac_out=cardiac_out,
        respiration_out=respiration_out,
        interp_style=interp_style,
        fir_order=fir_order,
        quiet=quiet,
        demo=demo,
        show_graphs=show_graphs,
        debug=debug,
        slice_offset=slice_offset,
        slice_major=slice_major,
        slice_order=slice_order,
        zero_phase_offset=zero_phase_offset,
        legacy_transform=legacy_transform,
    )
    return retro_ts_py_execute(params, execution)


__all__ = [
    "RETRO_TS_PY_METADATA",
    "RetroTsPyOutputs",
    "RetroTsPyParameters",
    "retro_ts_py",
    "retro_ts_py_params",
]
